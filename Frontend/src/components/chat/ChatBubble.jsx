import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { Card } from "@/components/ui/card";

export default function ChatBubble({ role, message }) {
  const isUser = role === "user";

  return (
    <div
      className={`mb-6 flex items-start gap-3 ${
        isUser ? "flex-row-reverse" : ""
      }`}
    >
      <Avatar>
        <AvatarFallback>
          {isUser ? "U" : "AI"}
        </AvatarFallback>
      </Avatar>

      <Card className="max-w-3xl p-4">
        {message}
      </Card>
    </div>
  );
}