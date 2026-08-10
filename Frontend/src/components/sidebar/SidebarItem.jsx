export default function SidebarItem({ title }) {
  return (
    <button
      className="
        w-full
        rounded-lg
        px-3
        py-2
        text-left
        transition
        hover:bg-accent
      "
    >
      {title}
    </button>
  );
}