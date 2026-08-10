import { useState } from "react";
import api from "@/services/api";

const SESSION_ID = crypto.randomUUID();

export default function useChat() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Halo! Saya siap membantu Anda."
    }
  ]);

  const [loading, setLoading] = useState(false);

  const sendMessage = async (message) => {
    const userMessage = {
      role: "user",
      content: message
    };

    setMessages(prev => [...prev, userMessage]);

    setLoading(true);

    try {

      const response = await api.post("/chat", {

        session_id: SESSION_ID,

        message

      });

      setMessages(prev => [

        ...prev,

        {

          role: "assistant",

          content: response.data.reply

        }

      ]);

    } catch (error) {

      setMessages(prev => [

        ...prev,

        {

          role: "assistant",

          content: "Terjadi kesalahan saat menghubungi server."

        }

      ]);

    }

    setLoading(false);

  };

  return {

    messages,

    loading,

    sendMessage

  };

}