# MOP — Bottom-bracket-area creak diagnosis & correction

**Bike:** Trek Checkpoint SL 6 AXS Gen 2 (2023), 54 cm
**Assembly:** SRAM Rival 1 AXS crank, DUB Wide spindle, T47 threaded bottom bracket
**Symptom:** Sharp creak at crank positions 3 o'clock / 9 o'clock, **under load only**, reproducible statically (clipped in, braced, brakes locked). Pedals and cleats already ruled out by swap. Started immediately after a shop BB replacement.
**Doc rev:** 1 — 2026-08-30
**Estimated time:** 60–90 min
**Skill level:** intermediate home mechanic

---

## 1. Safety & ground rules

- Work with the bike in a stand. Chain will come off — have a Flattop quick link spare.
- **Warranty note:** this creak followed a paid service. Opening the BB yourself may end any recourse with the original installer, so if that matters, record a phone video of the static creak before starting.
- Do not exceed any torque value. Under-torque causes creak; over-torque cracks carbon or strips alloy. When in doubt, use the lower number and re-check.
- Keep DOT fluid, degreaser, and solvents off the brake rotors and pads.

## 2. References

| Doc | Where |
|---|---|
| SRAM Torque Specifications (authoritative numbers) | search "SRAM torque specifications pdf" on sram.com |
| SRAM DUB Cranksets & Bottom Brackets service manual | https://docs.sram.com/en-US/publications/7unL17qdyCWxTL38aPmYJ0/dub-cranksets-and-bottom-brackets |
| Trek Checkpoint SL Gen 2 service manual | trekbikes.com → manuals (IsoSpeed, thru-axle, seatpost) |
| Component diagram | `diagrams/sram-dub-crank-t47-bb.svg` in this repo |

## 3. Tools & materials

**Tools**
- 8 mm hex bit + torque wrench (range to ~55 N·m)
- T25 Torx bit
- 2 mm and 2.5 mm hex keys (preload collar clamp screw — check which yours takes)
- Low-range torque wrench (1–10 N·m) for chainring bolts and pinch bolt
- T47 bottom bracket wrench **matching the installed BB brand** — identify the brand off the cup face before buying (SRAM DUB T47, Wheels Mfg, Praxis, Kogel all differ)
- Soft mallet
- Bright work light, dental/bearing pick, calipers (optional)

**Materials**
- Bike grease (spindle splines, thread prep on non-structural fasteners)
- Anti-seize or assembly grease for the T47 threads
- Blue threadlocker (chainring bolts, rotor bolts)
- Friction/carbon assembly paste (optional, ring-to-spider face)
- Isopropyl alcohol, clean rags, nitrile gloves

## 4. Torque reference (verify against SRAM PDF / Trek manual)

| Fastener | Tool | Torque | Prep |
|---|---|---|---|
| T47 BB cups | T47 wrench | 35–45 N·m | anti-seize on threads |
| DUB crank bolt (self-extracting) | 8 mm hex | 38–54 N·m | light grease |
| Preload adjuster collar | hand | snug — zero play, cranks still spin free | — |
| Preload collar clamp screw | 2 / 2.5 mm hex | just snug (~1.5 N·m) — do **not** force | — |
| Chainring bolts ×8 (behind spider) | T25 | ~2.5 N·m (confirm) | blue threadlocker |
| Pedals into crank | 8 mm hex / 15 mm | 35 N·m | grease/anti-seize |
| Front & rear thru-axle | 6 mm hex | 12–15 N·m | grease threads + under head |
| Bottle cage bolts | 4 mm hex | 3 N·m | grease |
| 6-bolt rotor bolts | T25 | 6.2 N·m | blue threadlocker |
| Rear derailleur mounting bolt | T25 | ~4 N·m | — |
| Seatpost / dropper binder | 4 mm hex | start ~4 N·m, raise only until no slip | thin grease film |

---

## 5. Procedure

### Step 0 — Chain-slack isolation test (before any disassembly)

1. Shift to a mid gear. Push the derailleur cage forward to fully slacken the chain, or lift the chain off the ring onto the BB shell.
2. Brace, clip in, lock brakes, rock the cranks hard at 3/9 o'clock.
3. Record the result:
   - **Creak GONE with slack chain** → chain-tension path: chainring bolts, ring/spider interface, chain, cassette lockring, freehub, rear hub. Focus Steps 2 and 7.
   - **Creak STILL PRESENT** → spindle splines, BB cups/bearings, thread prep, or frame. Focus Steps 3–4.
4. Optional confirm: drip light oil at one junction at a time (cup-to-frame seam, behind chainring, pedal threads, seat collar). If the creak stops for a few minutes after wetting one joint, that joint is the source.

### Step 1 — Remove the crank

1. Loosen the **preload collar clamp screw** (2 / 2.5 mm hex) on the non-drive side. Back the collar off ~2 turns by hand.
2. If the non-drive arm has two T25 pinch bolts (most road DUB cranks do **not** — they rely on the self-extracting bolt), loosen both now.
3. 8 mm hex into the crank bolt. Unscrew — the self-extracting cap draws the non-drive arm off. Remove the arm.
4. Slide the drive-side crank + spindle out through the BB shell. Soft-mallet the spindle end if snug. **Note the feel** — it should slide, not fight.

### Step 2 — Chainring & spider (drive side, now exposed)

1. **Before touching a bolt:** inspect the ring-to-spider mating faces. Grey/black oxide paste or bright fretting scars = micro-movement = a prime creak source.
2. Remove the 8 T25 bolts **one at a time**. Clean each bolt + its threaded hole with isopropyl. One drop blue threadlocker. Reinstall finger-tight.
3. If fretting was present: separate the ring, clean both faces, thin film of anti-seize or friction paste on the contact land only (not the bolt seats), reassemble.
4. Torque the 8 bolts in a star pattern, two passes, to spec (~2.5 N·m — confirm).
5. Grab the ring at 12 and 6 o'clock and try to rock it on the spider. Any movement = not fixed; revisit face prep.
6. Inspect the spindle-to-spider junction on the drive arm for cracks or movement (rare — warranty item if found).

### Step 3 — Spindle & bearings

1. Wipe the **spindle splines** clean. Look for galling, wear, or a dry scuffed appearance.
2. Spin each BB bearing with a fingertip: must be smooth and silent. Notchy / gritty / rough = contaminated during install (common if the bike was pressure-washed afterward).
3. Push–pull and rock each bearing radially. Any play = bearing or seat is bad.
4. Check bearing seals for purged grease or ingress of water/grit.

Rough bearings or play → BB comes out (Step 4). Bearings perfect → still do Step 4's torque + thread check.

### Step 4 — T47 bottom bracket cups

1. Put the T47 wrench on each cup. Gently test in the **loosening** direction. Movement before ~35 N·m = it was under-torqued.
   - **Remember the drive-side cup is reverse (left-hand) thread.**
2. Remove both cups. Inspect:
   - Frame threads + cup threads must carry grease/anti-seize. **Bone-dry = the classic T47 creak.**
   - No galling, cross-threading, or alloy shavings. Cups should thread back most of the way **by hand**.
3. **Confirm the part.** Crank is DUB **Wide**. The BB must be a DUB Wide-compatible T47 (correct bearing bore/spacing). A standard road DUB BB under a Wide crank never fully stops creaking. If the installed unit is not clearly a Wide-spec BB, replace it with one that is.
4. Clean, fresh anti-seize on threads, reinstall, torque **35–45 N·m** (drive side reverse thread).

### Step 5 — Reassemble

1. Thin film of grease on the spindle splines and the non-drive arm bore.
2. Slide the drive-side crank + spindle through the shell.
3. Fit the non-drive arm. 8 mm hex, torque the crank bolt to **38–54 N·m**.
4. **Set preload:** thread the collar in by hand until it just contacts — **no lateral crank rock, cranks still spin freely**. Then tighten the clamp screw just enough to hold it (~1.5 N·m). If your crank uses non-drive pinch bolts instead, torque those to spec (~8–9 N·m).
5. Reinstall the chain (new Flattop quick link if broken).

### Step 6 — Retest

1. Brace, clip in, lock brakes, load the cranks hard at 3/9 both directions.
2. Ride under load out of the saddle.
3. **Acceptance:** no creak under static load and no creak on a loaded climb. If gone → done, log it (Step 8).

### Step 7 — If the creak survives Steps 1–6

Work these in order; retest after each:

1. **Seatpost / Reverb dropper** — pull it fully, clean seat tube + post, thin grease film, reinstall, binder torque low (just past slip). Re-test. Clears many phantom "BB" creaks.
2. **Saddle rail clamp** — check the dropper head bolts to spec, grease the rail cradle.
3. **Thru-axles** — remove front & rear, grease threads + under head, torque 12–15 N·m.
4. **Bottle cage bolts** — remove, grease, 3 N·m.
5. **IsoSpeed pivot** — check the decoupler bolt torque against the Trek manual; a dry IsoSpeed bearing creaks under pedaling load and gets blamed on the BB. Grease/replace bearings at interval if dry.
6. **Chain & quick link** — check wear with a Flattop-specific gauge; a worn or dry link ticks/creaks under load.
7. **Cassette lockring / freehub** — pull the cassette, grease the lockring threads and freehub body splines, torque lockring to spec.

### Step 8 — Close-out log

Record in `specs.md` or a maintenance log:
- Date, symptom, what was found, what fixed it
- Installed BB brand/model + confirmation it is DUB Wide spec
- Final torque values used
- Any parts ordered / replaced

---

## 6. Most likely root causes (this bike, this history)

Ranked, given "both arms, static-reproducible, immediately post-service":

1. Preload collar backed off or set wrong during the service
2. T47 cups installed dry / under-torqued
3. Crank spindle splines reinstalled dry
4. DUB Wide vs standard DUB BB mismatch
5. Chainring bolts disturbed / not threadlocked (if Step 0 pointed at the chain-tension path)
6. Contaminated BB bearing (if the bike was washed after the service)
