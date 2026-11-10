# Normal Form: a campus for database design

Learn database design by working through a small, fictional university campus. Normal Form (formerly
*Data Yard*) is a single-page browser app that covers a second-year Database Design course: ER modelling,
relational notation, normalization, relational algebra, SQL, MongoDB, JSON and XML. There is **nothing
to install and no database to set up**. Open `index.html` and start.

### [Open it: wrightjayn.github.io/data-yard](https://wrightjayn.github.io/data-yard/)

![Screens](docs/screens.jpg)

**Demo video (45s, original music):** [docs/demo.mp4](docs/demo.mp4)

## The campus

Each topic is a building on the campus map. Exercises are printed worksheets, and your work is marked
in the margin like a lecturer would: a tick and a note when you get it, a red-pen correction when you don't.

| Building | Topics |
|---|---|
| **Chen Hall** | Entities, attributes, relationships, cardinality, crow's foot notation, weak entities, generalization, ANSI/SPARC |
| **Codd Hall** | Relational notation (PK/FK), entity & referential integrity, functional dependency, 1NF → 4NF, relational algebra & calculus |
| **Boyce Laboratory** | Real SQLite in the browser: SELECT, WHERE, LIKE, GROUP BY/HAVING, JOINs, sub-queries, INSERT/UPDATE/DELETE, CREATE/ALTER |
| **Merriman Market Hall** | `find()` filters, `$gt` `$in` `$or` `$elemMatch`, dot notation, projection, sort/limit, insertOne/updateOne, embed vs reference |
| **Crockford House** | Syntax rules, data types, fixing broken JSON, writing JSON, table → JSON |
| **Goldfarb Archive** | Well-formed rules, elements vs attributes, JSON → XML, XPath, valid vs well-formed, hierarchical & network models |

The halls are named after the people behind each idea (Peter Chen, E. F. Codd, Raymond Boyce, Dwight Merriman,
Douglas Crockford, Charles Goldfarb). The names are used as building names only.

Plus:
- **Examination Hall:** a 12-question paper drawn from every building, marked once per question, graded A–F on a transcript.
- **The Workshop:** free practice with SQL, Mongo, JSON and XML, plus JSON ↔ XML conversion.

Each building has lecture notes (shown beside the worksheet on wide screens). You earn up to three marks per
exercise, plus XP, Years (levels) and streaks. There is a day (paper) and night (library) theme.
Progress is saved in the browser (`localStorage`).

## How the checking works

- **SQL:** your query runs on a fresh copy of the sample database ([sql.js](https://github.com/sql-js/sql.js), SQLite compiled to WebAssembly).
  The result is compared with the model answer's result, so any correct query passes, not just one exact spelling.
  For INSERT/UPDATE/DELETE/CREATE, the app compares the resulting table instead.
- **MongoDB:** a small built-in Mongo engine (no server) parses `db.students.find(...)` and similar commands, and compares the documents returned.
- **JSON / XML:** parsed with the browser's own `JSON.parse` / `DOMParser`, then checked against the expected data.

All student and staff names in the sample data are fictional.

## Use it

- **Offline:** download `index.html` and open it in any modern browser (desktop or phone). Without a connection it falls back to system fonts.
- **Online:** https://wrightjayn.github.io/data-yard/ (GitHub Pages, deployed from `main`).
- **Keyboard (desktop):** `Ctrl/⌘+Enter` run · `1–4` pick an option · `Enter` check · `H` hint · `Esc` back · `?` all shortcuts.

## Develop

The source is `src/game.html`. `index.html` is the built file, with the SQLite engine inlined so it works offline.
The visual design is specified in [`design.md`](design.md).

```bash
npm install        # fetches sql.js
npm run build      # writes index.html
```

To add an exercise, append an object to a building's `ch` array in `src/game.html`.
Types: `mcq`, `sort`, `build`, `sql`, `mongo`, `json`, `xml`. The app name is the `APP_NAME` constant.

## License

MIT
