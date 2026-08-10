import { useState } from "react";

import { Send } from "lucide-react";

import { Button } from "@/components/ui/button";

import { Textarea } from "@/components/ui/textarea";

import { useChat } from "@/context/ChatContext";

export default function ChatInput() {

    const [text, setText] = useState("");

    const {

        sendMessage,

        loading

    } = useChat();

    async function handleSend() {

        if (!text.trim()) return;

        await sendMessage(text);

        setText("");

    }

    return (

        <div className="border-t p-4">

            <div className="flex gap-3">

                <Textarea

                    value={text}

                    onChange={(e) =>

                        setText(e.target.value)

                    }

                    placeholder="Tanyakan sesuatu..."

                />

                <Button

                    disabled={loading}

                    onClick={handleSend}

                >

                    <Send />

                </Button>

            </div>

        </div>

    );

}