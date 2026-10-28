"""
Henter feltlista fra API-v2 inn i dokumentasjonen, så den aldri kopieres for hånd.

  python scripts/synk_fra_api.py /sti/til/API-v2

Kopierer docs/feltliste.xlsx til assets/feltliste.xlsx, og lager tabellene
assets/feltliste_{pub,ext,full}.{no,en}.md fra docs/feltliste_{pub,ext,full}.csv:
pub med alle felt, ext med feltene ext har i tillegg til pub, og full med toppfeltene full
har i tillegg til ext. Sidene «Felt på verket» henter tabellene inn. Kjør etter hver endring i
visningene (API-v2: scripts/export_feltliste.py), og legg resultatet i en PR her.
"""
import csv
import pathlib
import shutil
import sys

ROT = pathlib.Path(__file__).resolve().parent.parent
TYPE_EN = {"tekst": "text", "heltall": "integer", "liste": "list", "boolsk": "boolean", "objekt": "object",
           "tall": "number"}
NETT_EN = {"ja": "yes", "nei": "no", "delvis": "partly"}


def rad(*celler):
    return "| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in celler) + " |"


def kode(s):
    s = {"True": "true", "False": "false"}.get(s, s)
    return f"`{s}`" if s else "–"


def nett(verdi, lang):
    """«På Samlingen på nett»: tom celle betyr at feltet ikke er sammenlignet."""
    v = (verdi or "").strip()
    if not v:
        return "–"
    if lang == "en":
        for no, en in NETT_EN.items():
            if v.startswith(no):
                return en + v[len(no):]
    return v


def les(api, nivå):
    return list(csv.DictReader(open(pathlib.Path(api) / "docs" / f"feltliste_{nivå}.csv", encoding="utf-8")))


def kilde(r):
    """Første kildesti, uten språkhalen; resten er varianter av samme felt."""
    første = (r.get("kilde (object_collection)") or "").split(",")[0].strip()
    return første.removesuffix(".no").removesuffix(".en")


def tabell(rader, lang, med_nett=True):
    if lang == "no":
        hode = ["Felt", "Beskrivelse", "Type", "Eksempel", "Kilde i katalogen"] + (["På Samlingen på nett"] if med_nett else [])
    else:
        hode = ["Field", "Description", "Type", "Example", "Source in the catalogue"] + (["On the website"] if med_nett else [])
    ut = [rad(*hode), rad(*["---"] * len(hode))]
    for r in rader:
        typ = r["type"] if lang == "no" else TYPE_EN.get(r["type"], r["type"])
        celler = [f"`{r['felt']}`", r["beskrivelse (NO)"] if lang == "no" else r["description (EN)"], typ or "–",
                  kode(r.get("eksempel", "")),
                  kode(kilde(r) if lang == "no" else kilde(r).replace("bare publiserte bilder", "published images only"))]
        if med_nett:
            celler.append(nett(r.get("på Samlingen på nett", ""), lang))
        ut.append(rad(*celler))
    return "\n".join(ut) + "\n"


def main(api: str) -> int:
    shutil.copyfile(pathlib.Path(api) / "docs" / "feltliste.xlsx", ROT / "assets" / "feltliste.xlsx")
    pub, ext, full = les(api, "pub"), les(api, "ext"), les(api, "full")
    pub_felt = {r["felt"] for r in pub}
    ext_felt = {r["felt"] for r in ext}
    bare_ext = [r for r in ext if r["felt"] not in pub_felt]
    bare_full = [r for r in full if r["felt"] not in ext_felt and "." not in r["felt"]]
    for nivå, rader, med_nett in (("pub", pub, True), ("ext", bare_ext, True), ("full", bare_full, False)):
        for lang in ("no", "en"):
            (ROT / "assets" / f"feltliste_{nivå}.{lang}.md").write_text(tabell(rader, lang, med_nett), encoding="utf-8")
    print(f"{len(pub)} felt på pub, {len(bare_ext)} i tillegg på ext, {len(bare_full)} i tillegg på full; "
          "feltliste.xlsx kopiert")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "../API-v2"))
