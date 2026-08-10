export default function Header() {
  return (
    <header className="flex h-16 items-center justify-between border-b px-6">
      <div>
        <h1 className="text-xl font-semibold">
          AI Knowledge Assistant
        </h1>

        <p className="text-sm text-muted-foreground">
          RAG + Ollama + FastAPI
        </p>
      </div>
    </header>
  );
}