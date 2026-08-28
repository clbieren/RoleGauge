import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "RoleGauge — GitHub Skill Assessment",
  description: "Analyze GitHub profiles to assess developer skills for specific roles. AI-powered evidence detection with deterministic scoring.",
  keywords: ["github", "skill assessment", "developer evaluation", "role analysis"],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
