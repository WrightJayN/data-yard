# Normal Form: a campus for database design

Learn database design by working through a small, fictional university campus. Normal Form (formerly
*Data Yard*) is a single-page browser app that covers a second-year Database Design course: ER modelling,
relational notation, normalization, relational algebra, SQL, NoSQL, JSON and XML. Its 103 exercises follow
the question styles of recent CMP2018 final exams (ERD + relational notation, SQL + relational algebra,
normalisation to 4NF, and alternatives to databases). There is **nothing
to install and no database to set up**. Open `index.html` and start.

### [Open it: wrightjayn.github.io/data-yard](https://wrightjayn.github.io/data-yard/)

![Screens](docs/screens.jpg)

**Demo video (45s, original music):** [docs/demo.mp4](docs/demo.mp4)

## The campus

Each topic is a building on the campus map. Exercises are printed worksheets, and your work is marked
in the margin like a lecturer would: a tick and a note when you get it, a red-pen correction when you don't.

| Building | Exam question | Topics |
|---|---|---|
| **Chen Hall** (22) | Q1: ERD and relational notation | Scenario reading, attribute types, cardinality and participation in the lecture notation (diamonds, arrows = one, double lines = total), weak entities, unary/M:N relationships with attributes, aggregation, disjoint/total specialisation, ERD → relational notation; DBMS risks vs costs, DDLC, ANSI/SPARC |
| **Codd Hall** (19) | Relational model and normalisation | Entity and referential integrity on real tables, candidate vs primary keys, attribute vs domain, anomalies, FD true/false, dependency diagrams, partial/transitive/multi-valued dependencies, 1NF → BCNF → 4NF decompositions |
| **Boyce Laboratory** (29) | SQL and relational algebra | Exam-style schemas (firm, workshops, university) on real SQLite: UPDATE by %, LIKE `'%Pen%'` / `'_z%'`, MAX subqueries, GROUP BY/HAVING, LEFT JOIN counts, self-joins, CHECK and FOREIGN KEY constraints, ALTER … DEFAULT, CREATE VIEW. **Live relational algebra**: type π σ ⋈ × − ∪ ∩ ρ ← and it runs |
| **Merriman Market Hall** (14) | Alternatives to databases | NoSQL vs RDBMS, the four NoSQL families, column vs document stores, structured / semi-structured / unstructured data, keys and `$lookup` in MongoDB, a few live Mongo queries |
| **Crockford House** (9) | Alternatives to databases | Tables → JSON with nested objects for composite attributes and arrays for multivalued ones, grouped data, course documents |
| **Goldfarb Archive** (10) | Alternatives to databases | Well-formed XML with a declaration and one root, records, passages of text, grouped data, valid vs well-formed |

The halls are named after the people behind each idea (Peter Chen, E. F. Codd, Raymond Boyce, Dwight Merriman,
Douglas Crockford, Charles Goldfarb). The names are used as building names only.

Plus:
- **Examination Hall:** a 12-question paper drawn from every building, marked once per question, graded A–F on a transcript.
- **The Workshop:** free practice with SQL, relational algebra, Mongo, JSON and XML, plus JSON ↔ XML conversion.

Each building has lecture notes (shown beside the worksheet on wide screens). You earn up to three marks per
exercise, plus XP, Years (levels) and streaks. There is a day (paper) and night (library) theme.
Progress is saved in the browser (`localStorage`). Saves from before the exam-paper update keep their XP; their marks are reset because the exercises changed.

## How the checking works

- **SQL:** your query runs on a fresh copy of the sample database ([sql.js](https://github.com/sql-js/sql.js), SQLite compiled to WebAssembly).
  The result is compared with the model answer's result, so any correct query passes, not just one exact spelling.
  For INSERT/UPDATE/DELETE/CREATE, the app compares the resulting table instead, and constraint exercises test
  the constraint itself (for example, a negative salary must be rejected).
- **Relational algebra:** a small parser turns π σ ρ ⋈ × ∪ ∩ − and ← into SQL and runs it, with set semantics.
  Any equivalent expression passes; attribute order doesn't matter. ASCII forms (`-`, `<-`, `and`, `<>`) work too.
- **MongoDB:** a small built-in Mongo engine (no server) parses `db.students.find(...)` and similar commands, and compares the documents returned.
- **JSON / XML:** parsed with the browser's own `JSON.parse` / `DOMParser`, then checked against the expected data.
  XML checks accept elements or attributes, in any case, as long as the data is right.

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
Types: `mcq`, `sort`, `build`, `sql`, `ra`, `mongo`, `json`, `xml`. The app name is the `APP_NAME` constant.

## License

MIT
