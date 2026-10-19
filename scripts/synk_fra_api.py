"""
Henter feltlista fra API-v2 inn i dokumentasjonen, så den aldri kopieres for hånd.

  python scripts/synk_fra_api.py /sti/til/API-v2

Kopierer docs/feltliste.xlsx til assets/feltliste.xlsx, og lager tabellene
assets/feltliste_pub.no.md og assets/feltliste_pub.en.md fra docs/feltliste_pub.csv.
Sidene «Felt på verket» henter tabellene inn. Kjør etter hver endring i visningene
(API-v2: scripts/export_feltliste.py), og legg resultatet i en PR her.
"""
import csv
import pathlib
import shutil
import sys

ROT = pathlib.Path(__file__).resolve().parent.parent
TYPE_EN = {"tekst": "text", "heltall": "integer", "liste": "list", "boolsk": "boolean", "objekt": "object"}


def rad(*celler):
    return "| " + " | ".join(str(c).replace("|", "/") for c in celler) + " |"


def main(api: str) -> int:
    kilde = pathlib.Path(api) / "docs"
    shutil.copyfile(kilde / "feltliste.xlsx", ROT / "assets" / "feltliste.xlsx")
    rader = list(csv.DictReader(open(kilde / "feltliste_pub.csv", encoding="utf-8")))
    no = [rad("Felt", "Beskrivelse", "Type", "På Samlingen på nett"), rad("---", "---", "---", "---")]
    en = [rad("Field", "Description", "Type"), rad("---", "---", "---")]
    for r in rader:
        felt = f"`{r['felt']}`"
        no.append(rad(felt, r["beskrivelse (NO)"], r["type"], r.get("på Samlingen på nett", "")))
        en.append(rad(felt, r["description (EN)"], TYPE_EN.get(r["type"], r["type"])))
    (ROT / "assets" / "feltliste_pub.no.md").write_text("\n".join(no) + "\n", encoding="utf-8")
    (ROT / "assets" / "feltliste_pub.en.md").write_text("\n".join(en) + "\n", encoding="utf-8")
    print(f"{len(rader)} felt på pub; feltliste.xlsx kopiert")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "../API-v2"))
