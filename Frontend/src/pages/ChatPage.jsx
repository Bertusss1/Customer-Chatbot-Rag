import MainLayout from "@/components/layout/MainLayout";
import ChatWindow from "@/components/chat/ChatWindow";
import ChatInput from "@/components/chat/ChatInput";

export default function ChatPage() {

    return (

        <MainLayout>

            <div className="flex h-full flex-col">

                <ChatWindow />

                <ChatInput />

            </div>

        </MainLayout>

    );

}