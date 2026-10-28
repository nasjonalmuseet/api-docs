# Kom i gang

Denne veiledningen tar deg fra ingenting til et fungerende kall på ti minutter.

## 1. Lag en nøkkel

Gå til <https://api.nasjonalmuseet.no/api/v1/keys/register>. Fyll inn navn, e-post og hva du
skal bruke dataene til, les vilkårene og kryss av. Siden sjekker at du er et menneske uten
å bruke tredjepartstjenester.

- Nøkkelen **vises én gang**. Ta vare på den. Mister du den, lager du en ny.
- Den varer i **180 dager** og fornyes på samme side.
- Den gir nivået **pub**: publiserte verk, bilder og tekstsøk. Se [Tilgangsnivåer](../dokumentasjon/tilgangsnivaer.md).

## 2. Prøv i nettleseren

Åpne <https://api.nasjonalmuseet.no/api/docs>, trykk **Authorize** og lim inn nøkkelen.
Da kan du prøve hvert kall med **Try it out**, uten å skrive kode.

## 3. Ditt første kall

Nøkkelen sendes **alltid** i headeren `X-API-Key`.

=== "curl"

    --8<-- "forste-kall.sh"

=== "Python"

    --8<-- "forste-kall.py"

=== "JavaScript"

    --8<-- "forste-kall.js"

Svar (forkortet; `…` betyr at felt er utelatt):

```json
--8<-- "svar-verk.json"
```

Svaret er verket *Skrik* (NG.M.00939) som JSON. De viktigste feltene:

| Felt | Innhold |
|---|---|
| `nmId` | Verkets id, det samme som inventarnummeret |
| `mainTitle` | Hovedtittelen |
| `production[].person.name` | Kunstneren eller produsenten |
| `labelDate` | Dateringen slik den står på etiketten |
| `materialTechniqueDescription` | Materiale og teknikk |
| `primaryImage.imageUrl` | Hovedbildet, 1200 piksler bredt |

`lang=en` gir engelske verdier der katalogen har dem.

!!! warning "Fra en nettside"
    API-et tillater ikke kall direkte fra nettleseren (ingen CORS), og nøkkelen skal ikke
    ligge i kode som sendes til besøkende. Kall API-et fra din egen server, og send videre
    det nettsiden trenger. JavaScript-eksemplene er skrevet for Node.js 18 eller nyere.
    Unntak: IIIF-bildene og -manifestene, og Linked Art, kan hentes direkte.

## Vanlige feil

- **401 selv om du har nøkkel:** headeren heter `X-API-Key`. Andre navn, eller nøkkelen i adressen, virker ikke.
- **403 på et kall:** kallet krever et høyere nivå. Semantisk søk krever ext. Se [Tilgangsnivåer](../dokumentasjon/tilgangsnivaer.md).
- **Tom `mainTitle`:** verket har ingen publisert tittel. Bruk `objectName` (betegnelsen) som overskrift, slik nettsiden gjør.

## Neste steg

- [Finn verk](finn-verk.md): bla og søk
- [Bilder og IIIF](bilder.md)
- [Feilsvar og grenser](../dokumentasjon/feil-og-grenser.md)
