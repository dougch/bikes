# SKILLS.md — LeMond Poprad Disc maintenance skills

Maintenance skill index for the steel Poprad Disc, currently a 2x10 SRAM Force
commuter/gravel bike headed for a full rebuild (targeted summer 2026 — see `specs.md`
§7). Status key: ☐ not done · ◐ done once, need practice · ☑ confident

---

## 1. Steel frame rust prevention (frame saver)
Status: ☐ — **open issue**, see specs.md §1

- Skills: strip/dry the frame internally, apply an internal frame-protection oil
  (Frame Saver, boiled linseed oil, or similar) through the tube ends/vents, reseal
  cable ports and BB shell drain hole.
- Gotchas: do this **before** the rear-spacing cold-set (§3) and any repaint, since
  both involve internal frame work / heat. Don't skip the BB shell and head tube — the
  usual rust-out points on steel frames living somewhere wet.
- Tools: Frame Saver (or equivalent) with the long spray wand, rags, a way to plug/mask
  threaded holes before spraying.

## 2. Crankset & chainring replacement (SRAM Force, worn 39T)
Status: ☐ — **active issue**, chainring is done (skips, won't hold chain), see specs.md §1

- Skills: pull the crank (self-extracting bolt or crank puller depending on BB
  interface), swap chainring(s), re-torque crank bolt, check chainline against the new
  Ultegra BBR60 BB.
- Gotchas: this crank/chainring gets replaced for real once the Force22 groupset lands
  (specs.md §5) — a like-for-like 39T swap now is a stopgap only if the bike needs to
  ride before the rebuild.
- Tools: crank puller (if square-taper/older interface) or 8mm hex for a self-extractor,
  torque wrench, chain whip/lockring tool if the BB itself needs to come out too.

## 3. Bottom bracket service — English threaded (Shimano Ultegra BBR60)
Status: ☑ — installed 2025-08-19

- Skills: remove/install a threaded Hollowtech II BB, grease threads, torque cups,
  check for creak/play after install.
- Gotchas: confirm shell width (68 vs 70 mm English — open item in specs.md §8) before
  ordering the Force22-compatible BB later. Standard threaded BB — much simpler than
  press-fit; if creak develops, re-grease threads first (same first move as the
  Checkpoint's T47 creak, see `trek_checkpoint/`).
- Tools: Shimano Hollowtech II BB tool (splined), torque wrench (BB torque per Shimano
  spec — typically ~35–50 Nm), grease.

## 4. Head tube / headset bearing service
Status: ☑ — bearings replaced 2021

- Skills: press out/in headset cups and bearings, check for play or notchiness, set
  headset preload, grease at service interval.
- Gotchas: last done 2021 — due for an inspection given the planned 2026 rebuild;
  cheap insurance to check bearing condition before repainting/rebuilding the frame.
- Tools: headset press (or shop service), headset preload/star-nut tools, grease.

## 5. Cable routing — install full-length housing/guides
Status: ☐ — **open issue**, see specs.md §1

- Skills: install missing braze-on or clamp-on cable guides, run full-length housing
  for shift/brake cables, dress and cap housing ends.
- Gotchas: do this as part of the rebuild rather than in isolation — final routing
  depends on the Force22 groupset choice (hydraulic front/rear brake hoses + mechanical
  shift cables) rather than the current 2x10 mechanical setup.
- Tools: housing cutter, cable end caps, ferrules, ruler for consistent loop lengths.

## 6. Rear triangle cold-setting (130 mm → 135 mm)
Status: ☐ — **planned**, see specs.md §0/§1

- Skills: cold-set (spread) steel dropouts to a wider spacing, check rear-end alignment
  (dropout parallelism) after spreading, re-face dropout faces if needed.
- Gotchas: steel tolerates this — the Stigmata's aluminum frame explicitly **cannot**
  be stretched (see `santacruz_stigmata/specs.md` §1), which is why this plan only works
  because the Poprad is steel. Spread gradually, check alignment with a dropout
  alignment gauge before declaring it done; a shop frame-alignment check is worth it
  given this determines whether the new hub/axle fits cleanly.
- Tools: dropout spreader (or careful by-hand technique with alignment checks),
  dropout alignment gauge, frame align table access if available.

## 7. Mechanical disc brake service (front/rear, current build)
Status: ☐

- Skills: pad swap, cable-actuated caliper pad-gap adjustment, rotor truing, bed-in.
- Gotchas: confirm caliper make/model first (specs.md §8) — if it's an Avid BB7, the
  Road vs Mountain distinction matters for lever-pull compatibility, same check done
  on the Stigmata's front BB7 (`santacruz_stigmata/SKILLS.md` §2).
- Tools: T25/5mm hex depending on caliper, rotor truing fork, isopropyl, spare pads.

## 8. Hydraulic disc brakes — SRAM Force22 (post-rebuild)
Status: ☐ — not yet applicable; needed once the Force22 groupset is installed (specs.md §5)

- Skills: bleed (SRAM Bleeding Edge, DOT 5.1 fluid), pad swap, bed-in, lever reach/contact adjust.
- Gotchas: **DOT fluid, not mineral oil** — same family as the Checkpoint's Rival AXS
  brakes (`trek_checkpoint/SKILLS.md` §4); same bleed kit and fluid work here.
- Tools: SRAM Bleed Kit, DOT 5.1, T10/T25, pad spreader, isopropyl.

## 9. Wheel build / tubeless conversion planning
Status: ☐ — planning stage, see specs.md §5/§7

- Skills: evaluate hub/freehub compatibility (Shimano HG, QR, 135 mm spacing) before
  ordering, tubeless-tape a non-TLR rim if the chosen wheels aren't factory tubeless,
  mount and seat tubeless WTB Barlow Pass tires.
- Gotchas: this bike's whole upgrade path hinges on staying QR (see specs.md §7 — AXS
  Rival is a dead end here). Double-check any wheelset or custom build spec is QR,
  135 mm rear, and takes an 11-speed cassette before committing money.
- Tools: tubeless tape (rim-width matched), valve core tool, sealant, tubeless
  pump/booster, tire levers.

## 10. Toe-overlap mitigation & cockpit fit
Status: ☐ — **open issue**, see specs.md §1/§5

- Skills: measure actual toe-overlap distance, evaluate crank length change (170 →
  165/160 mm) as a fix, adjust cleat fore/aft position, re-check with the actual shoes
  used.
- Gotchas: this is a geometry issue on this frame/size — it can be reduced (shorter
  cranks, cleat position, being mindful at low speed) but not fully eliminated without
  a different frame. Plan the crank-length choice in specs.md §5 together with this.
- Tools: tape measure, cleat tool, the actual shoes ridden (fit changes with shoe sole shape).

## 11. Fender fit & mounting
Status: ◐ — fenders fit well (DIY + 3D-printed), rear mount still slides (specs.md §2/§7)

- Skills: fabricate/print fender mount hardware, secure the rear fender so it stops
  shifting, media-blast and refinish (anodize/paint) as planned.
- Gotchas: whatever rear-fender fix goes in should survive the 135 mm respacing and any
  new wheel/tire width — don't finalize the mount until the wheel/tire plan (§9) is set.
- Tools: 3D printer + files, mounting hardware (stainless bolts/P-clips), media
  blasting/anodizing access (likely outsourced).

---

## Recurring maintenance calendar (adjust to mileage/commute frequency)

| Interval | Task |
|---|---|
| Every ride | Tire pressure, quick brake check, wipe chain |
| Weekly (commuting) | Clean/relube drivetrain, check for play, wipe frame dry after wet rides |
| Monthly | Chain wear gauge, brake pad check, bolt-torque spot check |
| ~6 months | Headset play check, BB check, cable/housing inspection |
| Annually | Frame-saver reapplication check, full drivetrain inspection, fender hardware check |

## Rebuild checklist (summer 2026 target — see specs.md §7)
- [ ] Apply frame saver (§1) — before cold-setting or repaint
- [ ] Cold-set rear to 135 mm (§6)
- [ ] Confirm BB shell width, order Force22-compatible BB (§3)
- [ ] Source Force22 groupset (crank 165/170 mm, 11-32 cassette) (specs.md §5)
- [ ] Source/build 135 mm QR wheelset, Shimano HG freehub (§9)
- [ ] Mount tubeless Barlow Pass tires (§9)
- [ ] Install full-length cable guides + route new housing/hoses (§5)
- [ ] Bleed Force22 hydraulic brakes (§8)
- [ ] Media blast + refinish fenders, fix rear mount (§11)
