# design.md — Data Yard redesign brief

> **For Claude:** This is a visual and UX redesign of the existing game in
> `src/game.html` (repo `WrightJayN/data-yard`). Change how it looks, reads
> and flows. Do **not** change what it teaches or how answers are checked.
> Read the whole brief before editing, then work through the
> [Implementation order](#12-implementation-order) and tick off the
> [Acceptance checklist](#13-acceptance-checklist).

---

## 1. Goal

Make the game appeal to **university students** (CMP2018 Database Design).
Today it looks like a children's learning app: navy cards, rounded Fredoka
type, emoji icons and confetti. The two problems to fix are:

1. **It looks childish.**
2. **It has no identity.** Nothing about it is memorable or ownable.

**New direction:** *editorial / campus*. The app becomes a small, fictional
university campus. Each topic is a building. Exercises look like printed
worksheets, and feedback looks like a lecturer marking your work in the
margin. It should feel considered, warm and grown-up, like a good
independent study tool and not a kids' game. The game layer stays, but it is
quieter.

**Design principles**
- **Print first.** Use paper, ink, rules, numbered exercises and margin
  notes. Typography and layout carry the character, not gradients or emoji.
- **Earned, not loud.** Rewards are real but understated. No confetti.
- **Always know where you are.** Each building has its own ink colour,
  carried through every screen inside it.
- **Phones first.** Most use is on a phone between classes. Laptops get a
  richer two-column layout as an enhancement.

---

## 2. Hard constraints (do not break)

- **Single file.** All markup, CSS and JS stay in `src/game.html`. Rebuild
  `index.html` with `npm install && npm run build` (placeholders
  `/*__SQLJS__*/` and `/*__WASM__*/` must survive). No frameworks and no new
  runtime dependencies.
- **Logic is frozen.** Do not edit challenge content (`ch` arrays), lesson
  text, the answer checkers, the SQL (sql.js), Mongo, JSON or XML engines,
  scoring maths, unlock rules or Exam question selection. Re-skinning the
  markup that these functions output is fine. Changing what they decide is not.
- **Keep saved progress.** Keep the localStorage key `datayard_v1` and every
  existing field of `S`. New preferences (for example `S.theme`) are added as
  optional fields with defaults.
- **Keep the URL.** Do not rename the repo or move `index.html`. The live
  site stays at `https://wrightjayn.github.io/data-yard/` even though the app
  gets a new name (§3).
- **Privacy rule.** No real names of students, staff or the user anywhere.
  All sample data stays fictional (Alex Watson, Ms. Grant, Mr. Bailey,
  Mr. Clarke, Ms. Douglas, Dr. Patel …). Hall names honour **published
  database pioneers only** (§4). Use them as building names only, with no
  portraits, likenesses or biographies drawn in the UI. Commits are authored
  as "Claude".
- **Fonts.** Load from Google Fonts as the app does now, always with
  system fallbacks so the app stays usable offline.

---

## 3. Name and brand

The app is being **renamed**. Put the name in a single constant,
`const APP_NAME = '…'`, and use it everywhere (wordmark, `<title>`, loading
text, result cards, README heading).

**Recommended: _Normal Form_**. It's a database pun (1NF–4NF) that also
reads like a school ("the Form"), and it's short enough for a wordmark.

| Option | Why |
|---|---|
| **Normal Form** *(default)* | A pun on normalisation and on school forms. Crest line: "Est. 1970", the year Codd published the relational model. |
| Schema College | Plain and descriptive, clearly about databases. |
| Key & Query | A friendly two-part name that suits a crest. |
| Codd College | Named for the relational model's author. Ties the halls together. |

The user picks the final name. Until then use **Normal Form**.

**Tagline:** "A campus for database design."

**Logo:** a crest or seal drawn as an inline SVG in the engraved style (§7).
It's a shield or roundel containing a simple cylinder (the database glyph)
crossed with a key, with a ribbon carrying the name and "EST. 1970". It uses
`currentColor` only, so it themes automatically. It needs a 32 px favicon
version (simplified) and a 120 px home-screen version.

**Wordmark:** the name in Space Grotesk 700, uppercase, tracked +4%. The
tagline sits underneath in mono caps.

---

## 4. Information architecture: the campus

The six worlds become **six named halls** plus the Examination Hall and a
workshop (Sandbox). The data stays the same. Only the display names, icons
and colours change. Map each world object to new display fields (for example
add `hall`, `short`, `ink`, `inkNight`, `art`) rather than renaming its
existing keys.

| Old world | New building | Named for | Short label | Topic line |
|---|---|---|---|---|
| ER Bay | **Chen Hall** | Peter Chen, ER model (1976) | Chen | Entities, relationships, diagrams |
| Relation Ridge | **Codd Hall** | E. F. Codd, relational model (1970) | Codd | Relations, keys, normal forms, algebra |
| SQL Lab | **Boyce Laboratory** | Raymond Boyce, co-designer of SQL | Boyce Lab | Live SQL |
| Mongo Market | **Merriman Market Hall** | Dwight Merriman, MongoDB co-founder | Market Hall | Documents and queries |
| JSON Junction | **Crockford House** | Douglas Crockford, popularised JSON | Crockford | JSON syntax and structure |
| XML Cove | **Goldfarb Archive** | Charles Goldfarb, created GML/SGML (XML's ancestor) | Archive | XML, XPath, older data models |
| Exam Boss | **Examination Hall** | none | Exam Hall | 12-question paper, graded A–F |
| Sandbox | **The Workshop** | none | Workshop | Free SQL / Mongo / JSON / XML |

**Vocabulary changes**

| Old | New |
|---|---|
| World | Building / Hall |
| Challenge 4 of 13 | **Exercise 04 / 13** |
| Lesson cards | **Lecture notes** |
| Back to map | **Back to campus** |
| Stars | **Marks** (★ glyphs stay, drawn in the engraved style) |
| World complete | **Certificate of completion** |
| Exam Boss / Fight again | **Examination Hall / Sit again** |
| Level | **Year** (Year 1, Year 2 … the same thresholds as levels) |

---

## 5. Visual system

### 5.1 Themes

Day ("paper") is the default. Night ("library at night") is a full theme,
not an inverted day theme. Default to `prefers-color-scheme`, remember the
user's choice in `S.theme` (`'day' | 'night' | 'auto'`), and set it on
`<html data-theme>`. The toggle is a small sun/moon line icon in the top bar.

### 5.2 Colour tokens

Replace the current `:root` palette. All text pairs below were checked
against WCAG AA (contrast ratio on page background / on card).

| Token | Day | Night | Use |
|---|---|---|---|
| `--paper` | `#F4EFE6` | `#16140F` | page background |
| `--sheet` | `#FBF8F2` | `#211E17` | cards / worksheets |
| `--sheet-2` | `#EFE8DC` | `#2A261D` | inset areas, code blocks, keys |
| `--rule` | `#D9D0C1` | `#3A342A` | hairlines, borders |
| `--ink` | `#1C1A17` | `#EDE6D8` | body text (15.2 / 14.8) |
| `--ink-2` | `#6B645A` | `#A39C8E` | secondary text (5.1 / 6.8) |
| `--accent` | `#A63A0A` | `#F59E0B` | primary buttons, links, focus (5.7 / 8.6) |
| `--on-accent` | `#FBF8F2` | `#16140F` | text on accent buttons |
| `--redpen` | `#B91C1C` | `#F87171` | wrong-answer marks (5.7 / 6.7) |
| `--tick` | `#166534` | `#4ADE80` | correct ticks, "approved" (6.2 / 10.6) |
| `--pencil` | `#8A8275` | `#7D7668` | hints, placeholders, decorative only |

**Building inks.** Set `--hall` on the screen root so every element inside a
building picks it up (header rule, exercise number, progress, key-bar
outline, illustration strokes).

| Building | Day `--hall` | Night `--hall` |
|---|---|---|
| Chen Hall | `#1E40AF` cobalt | `#93C5FD` |
| Codd Hall | `#6B21A8` plum | `#D8B4FE` |
| Boyce Laboratory | `#0F766E` teal | `#5EEAD4` |
| Market Hall | `#3F6212` olive | `#BEF264` |
| Crockford House | `#854D0E` ochre | `#FCD34D` |
| Goldfarb Archive | `#334155` slate | `#CBD5E1` |
| Examination Hall | `var(--ink)` | `var(--ink)` |

Every day building ink is at least 4.7:1 on `--paper`. Never use colour as
the only signal: pair it with the building name, the illustration and the
mark glyphs.

**Texture:** a very faint paper grain on `--paper` (an inline SVG
`feTurbulence` noise at about 3–4% opacity, as a data-URI background). In
night mode use about 2%. No gradients on surfaces.

### 5.3 Typography

| Role | Font | Spec |
|---|---|---|
| Display / headings | **Space Grotesk** 500/700 | H1 32/36 (phone 28/32), H2 22/28, H3 18/24, letter-spacing −0.01em. Building names uppercase, tracked +0.04em |
| Body / UI | **Inter** 400/500/600 | 16/1.6 body, 15 px buttons, 13 px captions |
| Labels, numbers, code | **JetBrains Mono** 400/600 | Labels in mono caps 11–12 px, tracked +0.08em (`EXERCISE 07 / 16`, `SQL QUERY`). Code 14.5 px / 1.55 |
| Margin annotations | **Caveat** 600 | 20–22 px, rotated −2°, coloured `--redpen` or `--tick` |

Font stack fallbacks: `'Space Grotesk', ui-sans-serif, system-ui`;
`Inter, system-ui, sans-serif`; `'JetBrains Mono', ui-monospace, Menlo,
monospace`; `Caveat, 'Bradley Hand', cursive`. Remove Fredoka and Nunito.

Numbers that matter (XP, scores, exercise numbers) always use mono with
`font-variant-numeric: tabular-nums`.

### 5.4 Shape, space, elevation

- **Radius:** 4 px for cards and inputs, 2 px for chips and keys, 999 px only
  for the theme toggle. Square-ish corners replace the current 12–14 px
  bubbles.
- **Borders over shadows.** Use 1 px `--rule` borders. One shadow token for
  sheets: `0 1px 0 var(--rule), 0 8px 24px -12px rgba(28,26,23,.18)`. Night
  mode uses no shadow, only a border.
- **Spacing scale:** 4, 8, 12, 16, 24, 32, 48. Phone gutter 16 px, card
  padding 20 px.
- **The worksheet.** Exercise cards have a thin vertical margin rule
  (1 px `--redpen` at 25% opacity) 28 px from the left edge on phones and
  56 px on desktop, like an exercise book. Exercise numbers sit in that
  margin, and annotations land there (§8).

### 5.5 Buttons and inputs

- **Primary** (Check, Next, Begin): solid `--accent`, `--on-accent` text,
  Inter 600, min-height 48 px, full width in the bottom dock.
- **Secondary** (Run, Tables, Target, Clear): 1 px `--ink` outline,
  transparent fill, line icon and label. Min-height 44 px.
- **Tertiary / text:** underlined `--accent` link style.
- **Pressed state:** translateY(1px) and a darker fill. **Focus:** a 2 px
  `--accent` outline offset by 2 px, always visible on keyboard focus.
- **MCQ options:** full-width rows on `--sheet`, 1 px `--rule`, with a mono
  letter (A–D) in a 28 px square on the left. Selected: `--hall` border plus
  a filled letter square. After checking, the correct row gets a `--tick`
  border and a ✓, and the wrong pick gets a red-pen strike-through (§8).
- **Code editor** (`textarea.ed`): `--sheet-2` background, 1 px `--rule`,
  4 px radius, JetBrains Mono. Focus is a 2 px `--hall` left border plus the
  focus ring. Keep the existing key bar, restyled as mono "typewriter keys"
  (2 px radius, 1 px border, `--sheet`).
- **Result tables:** mono 13 px, header row in mono caps on `--sheet-2`,
  hairline row rules, no zebra stripes.
- **Errors** (`.err`): a `--sheet` block with a 3 px `--redpen` left border
  and mono text. No pink fill.

---

## 6. Iconography

Replace **every** emoji (world icons, 🔥, 🗂, 🎯, 💡, 👑, ✅, ▶ labels …)
with inline SVG.

- **UI icons:** a single thin-line set, 1.5 px stroke at 24 px,
  `stroke="currentColor"`, round caps. Draw them in the Lucide style (or
  inline the matching Lucide paths, which are MIT). The set needs: back, sun,
  moon, hint (pencil), run (play), table, target, documents, check, x, reset,
  convert, lock, flame (streak), clock (exam), menu, external.
- Build a tiny helper `icon(name)` that returns the SVG string, and keep the
  path data in one object.

---

## 7. Illustration style: engraved

Each building gets a small hand-built **engraved / etched SVG vignette**.
Think of the line-and-hatching drawings in old university prospectuses:
outlines plus parallel hatching for shade, drawn in `currentColor` so they
take the building ink in both themes.

- **Sizes:** a 96×96 map building and a 320×140 building header banner.
  Both come from the same drawing, with the banner adding ground and trees.
- **Technique:** strokes 1–1.25 px, hatching made with a reusable `<pattern>`
  of diagonal lines at 4–5 px spacing, and one accent stroke weight for
  outlines. No fills except `--sheet` behind the building to knock out map
  paths.
- **Each building has its own architecture, reflecting the topic:**
  - *Chen Hall:* a two-wing hall joined by a covered walkway (a relationship
    between entities), with diamond-shaped windows over the door.
  - *Codd Hall:* a classical façade with columns laid out like a table
    (rows and columns), with a pediment.
  - *Boyce Laboratory:* a modern lab with a chimney or flask silhouette and
    a big grid of windows.
  - *Merriman Market Hall:* an open market hall with arches and hanging
    crates (documents).
  - *Crockford House:* a narrow townhouse whose door frame forms `{ }`
    braces.
  - *Goldfarb Archive:* a tall archive with stacked tiers (a tree or
    hierarchy) and angle-bracket `< >` window arches.
  - *Examination Hall:* a domed hall with a clock face.
  - *The Workshop:* a low shed with a workbench and tools.
- **Never draw real people.** No portraits or busts of the people the halls
  are named after.
- Keep each drawing under about 3 KB, and keep all art in one `ART` object.

---

## 8. Feedback: the lecturer's margin

This replaces confetti and the bottom-sheet "Big up yourself!" panel.
Remove the `confetti()` function and its calls.

### Correct answer
1. The **margin annotation** draws in. A handwritten ✓ (an SVG path,
   animated with `stroke-dashoffset`, 350 ms) appears in the worksheet
   margin in `--tick`, followed by a Caveat note next to it, for example
   *"Big up! ★★★"*.
2. Below the exercise a **"Marker's note"** block slides open with a 1 px
   `--rule` top border, a mono caps label `MARKER'S NOTE`, the existing `why`
   explanation in Inter, and one line of mono stats:
   `+30 XP · ★★★ · streak 3`.
3. The primary button becomes **Next exercise →**.

Three marks gets one extra flourish: the ✓ is double-underlined. That's it.

### Wrong answer
1. **Red-pen correction.** The wrong MCQ option gets a hand-drawn
   strike-through. For code exercises, a red wavy underline appears under the
   editor or under the offending row or element when the checker can point
   to one. A short red circle-and-arrow in the margin points at it.
2. A Caveat margin note in `--redpen` gives the encouraging nudge, and the
   checker's existing message appears beneath it in Inter.
3. Tone: firm but kind. A lecturer who wants you to pass, not a red sea of
   marks. Show at most one mark at a time.

### Hint
The 💡 button becomes a **pencil** icon. The hint appears as a grey `--pencil`
Caveat note in the margin (on phones, under the prompt), like a lecturer's
pencilled aside.

### Mobile margin behaviour
On phones the margin is only 28 px wide. The mark (✓ or ✗ circle) sits in
the margin, and the handwritten note floats as a small annotation at the
card's top-right corner, overlapping the card edge by 8 px and rotated −2°.
On desktop, both live in a real 160 px right margin.

---

## 9. Game layer (subtler)

Keep XP, Years (levels), streaks, marks and completion, but restyle them as
academic record-keeping.

- **Top bar** (all screens): the crest at 24 px, the app name or building
  name, and on the right a mono `Y2 · 1,240 XP` plus the theme toggle. The
  streak shows as **tally marks** (`𝍸𝍸 ||`-style SVG strokes, maximum 7
  shown) with a small flame line icon. No large counters.
- **Exercise header:** mono caps `BOYCE LABORATORY` / `EXERCISE 07 / 16`, a
  1 px progress rule in `--hall` across the full width, and earned marks as
  three small engraved stars on the right.
- **Building complete:** a **Certificate of Completion** card styled like a
  printed certificate: a double-rule border, the crest, the building name and
  vignette, marks earned, the date, and *"Awarded to a student of
  {APP_NAME}"*. No personal name. Buttons: *Revisit building* / *Back to
  campus*.
- **Year up:** a slim banner under the top bar reading *"Promoted to Year 3."*
  It fades after 3 s. No modal.
- **Examination Hall** (Exam Boss): a cover page reading *"Examination Paper
  · 12 questions · All buildings"* with a **Begin examination** button. Use a
  numbered-paper look during the exam (`Q 04 / 12`, an optional subtle
  elapsed-time clock icon with mono time, no countdown pressure unless one
  already exists). The result is a **transcript** card: a table of buildings
  against marks, the letter grade A–F set huge in Space Grotesk 700 inside
  a stamped ring, and the best score.

---

## 10. Screens

### 10.1 Home: the campus map (phone first)

```
┌──────────────────────────────┐
│ ⛨ NORMAL FORM      Y2 · ☾    │  top bar (sticky)
├──────────────────────────────┤
│ ┌──────────────────────────┐ │
│ │ CONTINUE                 │ │  continue card (if any progress)
│ │ Boyce Laboratory         │ │  Space Grotesk 22, --hall rule
│ │ Exercise 07 · HAVING   → │ │
│ └──────────────────────────┘ │
│                              │
│  ╱ engraved campus map  ╲    │  scrollable SVG, ~390×900
│  Chen Hall ── The Quad ──    │  paths between buildings
│      │          │            │  each building = button
│  Codd Hall   Boyce Lab       │  progress flag under each:
│      │          │            │  "9/13 ★ 22"
│  Market Hall  Crockford      │
│        Goldfarb Archive      │
│      Examination Hall        │
│  ─────────────────────────── │
│  The Workshop  ·  Lecture notes │  footer links
└──────────────────────────────┘
```

- The map is one inline SVG drawn in the same engraved style: footpaths as
  dashed lines, a few hatched trees, a central quad with a sundial. Order
  the buildings top-to-bottom in course order so the natural scroll is the
  learning path. The path from a finished building to the next uses the
  building ink.
- Each building is a real `<button>` (or an `<a>` with role) with an
  accessible label, for example "Boyce Laboratory, SQL, 7 of 16 exercises,
  18 of 48 marks". Its hit area is at least 64×64 px.
- Under each building, show a mono caption with the short name and progress.
  Completed buildings get a small engraved pennant on the roof.
- Locked buildings (if the existing logic locks any) are drawn at 35%
  opacity with a lock icon, and a tap explains how to unlock them.
- First visit (no progress): the Continue card is replaced by a welcome
  card: *"Welcome to {APP_NAME}. Start at Chen Hall, where every database
  begins with a diagram."*

### 10.2 Building entrance

The building header banner (illustration) uses the building's `--hall` ink,
with the H1 building name, the topic line in mono caps, a progress rule,
and two actions: **Read the lecture notes** (secondary) and **Begin
exercises / Continue at 07** (primary). Below, list the exercises as
numbered rows (`01  Identify the entities  ★★☆`) so students can jump
straight to any exercise they have unlocked.

### 10.3 Lecture notes (lesson cards)

Present each card as a page of notes: a mono caps label `LECTURE NOTES · 2 / 5`,
a Space Grotesk heading, Inter body at a 16/1.65 measure capped at 62ch,
code in `--sheet-2` blocks, and key terms in a `--hall`-coloured
semi-bold. Use the bottom dock for Previous / Next, and on the last card
*Begin exercises →*. Keep the existing diagrams (the crow's-foot SVGs) but
restyle their strokes to `--ink` and fills to `--sheet`, so they look
printed.

### 10.4 Exercise (the worksheet)

```
┌──────────────────────────────┐
│ ‹  BOYCE LABORATORY   ★★☆    │
│    EXERCISE 07 / 16          │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │ ← --hall progress rule
│┃                             │
│┃ SQL QUERY                   │ ← mono caps type label
│┃ Show each major and its     │ ← Inter 18/1.5 prompt
│┃ average GPA, but only       │
│┃ majors whose average GPA    │
│┃ is above 3.3.               │
│┃ ┌─────────────────────────┐ │
│┃ │ SELECT major, AVG(gpa)  │ │ ← editor
│┃ │ FROM student            │ │
│┃ └─────────────────────────┘ │
│┃ [SELECT][*][FROM][WHERE]…   │ ← key bar
│┃ [▷ Run] [▦ Tables] [◎ Target]│
├──────────────────────────────┤
│ [✎]  [        Check        ] │ ← sticky dock
└──────────────────────────────┘
```

The ┃ is the margin rule from §5.4.

### 10.5 Workshop (Sandbox)

Use the same worksheet styling, with tabs in mono caps (`SQL · MONGO · JSON
· XML`) and an underline indicator in `--accent`. Keep the reset/schema/
convert actions as secondary buttons with line icons.

### 10.6 Desktop enhancement (≥ 1024 px)

- **Exercise:** a two-column grid of `minmax(320px, 420px) 1fr`. Left: a
  sticky **lecture notes** panel for the current building, scrollable, with
  the current topic highlighted. Right: the worksheet, with the 160 px
  annotation margin on its right edge. Max content width 1240 px, centred.
- **Campus:** the map gets more room (max 960 px wide). Hovering or
  focusing a building opens a side panel with its vignette, topic line,
  progress and a *Enter building* button.
- Keyboard shortcuts on desktop: `Ctrl/⌘+Enter` = Run, `Enter` on MCQ =
  Check after selecting, `1–4` = pick an MCQ option, `H` = hint, `Esc` =
  back. Show them in a small `?` overlay.
- Between 640 and 1023 px: a single column, max width 720 px, with the
  annotation margin at 96 px.

---

## 11. Voice and copy

Write in a **dry, smart, encouraging lecturer** voice with **occasional
Jamaican flavour**. Use local expressions as seasoning, about one message
in three, never in instructions or error explanations, where clarity wins.
Keep messages short.

**Correct (pick at random, weighted toward plain):**
"Correct." · "Tidy." · "Big up!" · "Clean work." · "Wicked." ·
"That's the one." · "Mi rate dat." · "Exactly right." · "Nuff respect."

**Three marks:** "Full marks." · "Big up yourself, full marks." ·
"Textbook."

**Wrong:** "Not quite. Check the margin." · "Close, but no." ·
"Almost. One thing's off." · "Easy nuh, look again." · "Try that once more."

**Exam results:** A: "Exam-ready. Big up!" · B: "Strong paper." ·
C: "Solid pass. Revisit the weaker halls." · D/E: "Not there yet. The
notes will get you there." · F: "Rough paper. Start with the lecture notes
and come back."

**Microcopy rules**
- Use sentence case everywhere except mono labels, which are caps.
- Buttons are verbs: *Check*, *Run*, *Next exercise*, *Begin examination*,
  *Back to campus*.
- Empty states and the loading line get a touch of character:
  *"Unlocking the campus…"*, *"Nothing run yet. Write a query and press
  Run."*
- Keep all sample data fictional (see §2).

---

## 12. Implementation order

1. **Tokens and themes.** Replace `:root` with the §5.2 tokens, add
   `[data-theme=night]`, the theme toggle and `S.theme`, swap the fonts, and
   add the paper grain.
2. **Base components.** Buttons, cards (worksheets with the margin rule),
   inputs, editor, key bar, tables, errors, chips, mono labels.
3. **Icons.** Add the `icon()` helper and replace every emoji.
4. **Naming layer.** Add `APP_NAME`, the per-world display fields (`hall`,
   `short`, `ink`, `inkNight`, `art`) and the vocabulary from §4. Update
   `<title>`.
5. **Illustrations.** Draw the crest, the eight building vignettes and the
   campus map SVG.
6. **Screens.** Home/campus → building entrance → lecture notes →
   exercise → completion certificate → Examination Hall and transcript →
   Workshop.
7. **Feedback.** Remove confetti, build the margin annotation system
   (correct, wrong and hint states) and the Marker's note block.
8. **Desktop layout** and keyboard shortcuts.
9. **Accessibility pass** (below).
10. **Copy pass:** replace the praise array and the strings in §11.
11. **Rebuild** `index.html`, then retake `docs/screens.jpg` (day and night,
    phone width) and update the README name, description and screenshots.
    Re-recording `docs/demo.mp4` is optional and can be done separately.

## 13. Acceptance checklist

**Accessibility (WCAG 2.1 AA)**
- [ ] Every text/background pair is at least 4.5:1 (body) or 3:1 (≥ 24 px
      or bold ≥ 19 px) in both themes. Re-check any new colours.
- [ ] Touch targets are at least 44×44 px (map buildings at least 64×64).
- [ ] All interactive elements are reachable and operable by keyboard in a
      logical order, with a visible focus ring.
- [ ] `prefers-reduced-motion: reduce` makes annotations appear instantly
      with no draw-in or slide animations.
- [ ] Map buildings, icons-only buttons and the theme toggle have
      accessible names. Decorative SVGs have `aria-hidden="true"`.
- [ ] Results are announced. Use an `aria-live="polite"` region for
      Correct / Not quite plus the explanation.
- [ ] Colour is never the only signal (✓ and ✗ glyphs, strike-through,
      text labels).
- [ ] Text zooms to 200% without loss of content. No fixed heights on text
      containers.

**Behaviour preserved**
- [ ] All 78 exercises still load, accept the same answers and award the
      same marks and XP.
- [ ] Existing saved progress under `datayard_v1` loads without loss.
- [ ] The SQL, Mongo, JSON and XML engines, the Workshop and the Exam all
      work, including offline after the first load (fonts fall back).
- [ ] `npm run build` produces a working `index.html`.

**Look and feel**
- [ ] No emoji, confetti, gradients, Fredoka or Nunito remain.
- [ ] Inside a building, the building ink appears on its header, progress
      rule, exercise number and illustration.
- [ ] Day and night both look intentional (check every screen in both).
- [ ] Tested at 360, 390, 768, 1024 and 1440 px widths.
- [ ] No real person's name or likeness appears anywhere except the hall
      names in §4.
