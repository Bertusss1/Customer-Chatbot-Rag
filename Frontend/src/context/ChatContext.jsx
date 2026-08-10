import { createContext, useContext, useState } from "react";
import api from "@/services/api";

const ChatContext = createContext();

const sessionId = crypto.randomUUID();

export function ChatProvider({ children }) {

    const [messages, setMessages] = useState([]);

    const [loading, setLoading] = useState(false);

    async function sendMessage(message) {

        const userMessage = {

            role: "user",

            content: message

        };

        setMessages(prev => [...prev, userMessage]);

        setLoading(true);

        try {

            const response = await api.post("/chat", {

                session_id: sessionId,

                message

            });

            setMessages(prev => [

                ...prev,

                {

                    role: "assistant",

                    content: response.data.reply

                }

            ]);

        } catch {

            setMessages(prev => [

                ...prev,

                {

                    role: "assistant",

                    content: "Server Error"

                }

            ]);

        }

        setLoading(false);

    }

    return (

        <ChatContext.Provider

            value={{

                messages,

                loading,

                sendMessage

            }}

        >

            {children}

        </ChatContext.Provider>

    );

}

export function useChat() {

    return useContext(ChatContext);

}