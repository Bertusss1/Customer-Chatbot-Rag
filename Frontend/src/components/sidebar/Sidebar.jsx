import { Plus } from "lucide-react";
import { Button } from "@/components/ui/button";
import SidebarItem from "./SidebarItem";

export default function Sidebar() {
  return (
    <aside className="flex w-72 flex-col border-r bg-muted/40">
      <div className="p-4">
        <Button className="w-full">
          <Plus className="mr-2 h-4 w-4" />
          New Chat
        </Button>
      </div>

      <div className="flex-1 space-y-2 overflow-y-auto px-3">
        <SidebarItem title="Chat tentang Python" />
        <SidebarItem title="Belajar FastAPI" />
        <SidebarItem title="RAG Project" />
      </div>
    </aside>
  );
}