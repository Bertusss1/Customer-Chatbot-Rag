import ChatBubble from "./ChatBubble";
import { useChat } from "@/context/ChatContext";

export default function ChatWindow() {

    const {

        messages,

        loading

    } = useChat();

    return (

        <div className="flex-1 overflow-y-auto p-6">

            {messages.map((message, index) => (

                <ChatBubble

                    key={index}

                    role={message.role}

                    message={message.content}

                />

            ))}

            {loading && (

                <ChatBubble

                    role="assistant"

                    message="Sedang berpikir..."

                />

            )}

        </div>

    );

}