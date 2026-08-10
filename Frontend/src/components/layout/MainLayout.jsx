import Header from "./Header";
import Sidebar from "../sidebar/Sidebar";

export default function MainLayout({ children }) {
    return (
        <div className="flex h-screen">

            <Sidebar />

            <div className="flex flex-1 flex-col">

                <Header />

                <main className="flex-1 overflow-hidden">

                    {children}

                </main>

            </div>

        </div>
    );
}