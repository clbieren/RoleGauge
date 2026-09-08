import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "SkillLens — Geliştirici Profil Değerlendirme",
  description:
    "GitHub projelerinin hedeflediğin role beklenen becerilerle ne kadar örtüştüğünü gör. Kanıt tabanlı değerlendirme.",
  keywords: [
    "github",
    "beceri değerlendirme",
    "developer assessment",
    "profil analizi",
    "yazılımcı",
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="tr">
      <body>{children}</body>
    </html>
  );
}
