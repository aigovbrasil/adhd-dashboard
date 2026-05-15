# ADHD Desk Dashboard Skill

## Purpose
Create low-cognitive-load operating dashboards for a solo knowledge worker with ADHD/TDAH and dyslexia constraints, using printable A4 landscape artifacts plus simple digital backlog structures.

The skill converts a messy operational request into a clean physical-digital workflow system: sprint dashboard, capacity table, daily workflows, research capture card, print checklist, and Linear backlog.

## When to Use
Use this skill when the user asks for:
- ADHD/TDAH-friendly workflow design.
- Printable dashboards, desk boards, paper operating systems, or A4 landscape templates.
- Low-code workflow orchestration using Linear, Drive, Calendar/Agenda, Claude/ChatGPT, GitHub, and paper.
- Daily execution systems with explicit Definition of Done.
- Cognitive-load reduction for research, content, admin, and data-cleaning routines.

## Inputs
Expected inputs may include:
- Raw command or workflow brief.
- Current stack: Linear, Drive, Calendar, Claude/ChatGPT, GitHub, social channels, paper.
- Target routines: DataClean, Content Creation, Ops Admin, Analytics, Review.
- Accessibility constraints: large text, minimal visual noise, high legibility, clear labels, printable format.
- Delivery format: PPTX, PDF, Markdown checklist, Linear issue plan.

## Outputs
The standard output bundle is:
1. `leonardo-desk-dashboard.pptx` — A4 landscape dashboard deck.
2. `leonardo-desk-dashboard.pdf` — print-ready PDF.
3. `checklist-impressao.md` — print and desk setup checklist.
4. `linear-issues-dashboard.md` — Linear project, labels, recurring issues, and views.
5. `README.md` — usage documentation.
6. `sources-and-safety.md` — ADHD/TDAH evidence and non-clinical boundary.

## Operating Principles
- Reduce cognitive load before adding automation.
- Use one objective per page or card.
- Prefer boxes, tables, and explicit fields over paragraphs.
- Use large typography: body ≥14pt, headers ≥18pt.
- Keep every slide standalone and printable.
- Use explicit labels: FACT, HYPOTHESIS, DECISION, ACTION.
- Every workflow must have a visible Definition of Done.
- Do not provide diagnosis, medication advice, or clinical claims.

## Default Slide Architecture
| Slide | Name | Function | Required Blocks |
|---|---|---|---|
| S1 | Roadmap Mesa | Weekly sprint control | Objective, priority, deliverables, risks, DoD, next action |
| S2 | Capacity Table | Daily workflow allocation | Workflow, time, priority, input, output, save location, command, DoD |
| S3 | WF1 Data Clean | 45-minute data processing | Raw, classify, extract, save, Linear, command, DoD |
| S4 | WF2 Content | Morning content routine | Topic, update, batch, reuse, channel, agenda, DoD |
| S5 | WF3 Ops Admin | 90-minute admin loop | Login, email, accounts, GitHub, social, Linear, agenda, external admin, DoD |
| S6 | Research Card | Manual research capture | Research, finding, number, source, hypothesis, decision, action, tag, reuse, priority |

## Design Requirements
- Page: A4 landscape, 297 × 210 mm.
- Margins: 15 mm.
- Background: neutral, non-decorative.
- Fillable fields: light gray `#F5F5F5`.
- Use sans-serif fonts.
- Avoid dense bullet lists.
- Avoid decorative ribbons, gradients, clip art, or ornamental icons.
- Optimize for black-and-white printing when possible.

## Execution Protocol
1. Parse the raw request.
2. Identify target user, constraints, stack, workflows, outputs, and risks.
3. Convert the request into a MECE workflow map.
4. Define one physical page per execution context.
5. Add DoD to every page.
6. Generate artifacts.
7. Validate legibility, printability, and lack of overlap.
8. Export final package.

## Safety Boundary
This skill supports planning, organization, workflow design, and accessibility-oriented formatting. It is not a medical diagnostic tool and must not advise medication, clinical treatment, or self-diagnosis. For clinical ADHD/TDAH concerns, direct the user to a qualified health professional.
