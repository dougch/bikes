#!/usr/bin/env python3
"""Generate .ics files for the 2026 Cross Revolution Cyclocross series (my start wave).

Source: https://cross-revolution.com/ (schedule + #venues)

Start wave: 9:15 AM. ASSUMPTION -- confirm this is the right wave before
trusting the times below.

Unlike the MFG series page, Cross Revolution's site does not publish a
separate "staging" clock time -- only a race START time. Events below use
the published start time as DTSTART; the 1-hour VALARM is a generic
arrive-and-register reminder, not an official staging call time.

Race #1 (Sacajawea Park, 2026-09-20) already happened by the time this was
generated (2026-09-21) and is intentionally omitted.
"""

from dataclasses import dataclass
from pathlib import Path

TZID = "America/Los_Angeles"

VTIMEZONE = """BEGIN:VTIMEZONE
TZID:America/Los_Angeles
BEGIN:DAYLIGHT
TZOFFSETFROM:-0800
TZOFFSETTO:-0700
TZNAME:PDT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:-0700
TZOFFSETTO:-0800
TZNAME:PST
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
END:STANDARD
END:VTIMEZONE"""


@dataclass(frozen=True)
class Race:
    slug: str
    name: str
    date: str  # YYYYMMDD
    venue: str
    location: str
    geo: str
    address_source: str
    register_url: str
    notes: str


RACES: list[Race] = [
    Race(
        slug="02-steel-lake",
        name="CXR #2 - Steel Lake",
        date="20261018",
        venue="Steel Lake",
        location="2410 S 312th St, Federal Way, WA 98003",
        geo="",
        address_source="street address published on race page",
        register_url="https://www.bikereg.com/cross-revolution-2026-race-2-steel-lake",
        notes="",
    ),
    Race(
        slug="03-celebration-park",
        name="CXR #3 - Celebration Park (Cole Meckle Memorial)",
        date="20261101",
        venue="Celebration Park",
        location="1095 S 324th St, Federal Way, WA 98003",
        geo="",
        address_source="street address published on race page",
        register_url="https://www.bikereg.com/cross-revolution-2026-race-3-celebration-park",
        notes="Run in memory of Cole Meckle.",
    ),
    Race(
        slug="04-frontier-park",
        name="CXR #4 - Frontier Park (St. Jude's Classic)",
        date="20261115",
        venue="Frontier Park",
        location="21718 Meridian E, Graham, WA 98338",
        geo="",
        address_source="street address published on race page",
        register_url="https://www.bikereg.com/cross-revolution-2026-race-4-frontier-park",
        notes="Charity race benefiting St. Jude Children's Research Hospital.",
    ),
    Race(
        slug="05-kelley-farm",
        name="CXR #5 - Kelley Farm",
        date="20261129",
        venue="Kelley Farm",
        location="20021 Sumner-Buckley Hwy E, Bonney Lake, WA 98391",
        geo="",
        address_source="street address published on race page; new venue for 2026",
        register_url="https://www.bikereg.com/cross-revolution-2026-race-5-kelley-farm",
        notes="Season finale -- awards ceremony after racing.",
    ),
]

START = "091500"
END = "095500"  # 9:15 start + 40 min race
START_LABEL = "9:15 AM"
DURATION_LABEL = "40 min"


def fold(line: str) -> str:
    """Fold lines at 75 octets per RFC 5545."""
    out = line[:75]
    rest = line[75:]
    while rest:
        out += "\r\n " + rest[:74]
        rest = rest[74:]
    return out


def vevent(race: Race) -> str:
    desc_parts = [
        f"Start: {START_LABEL}",
        f"Race length: {DURATION_LABEL}",
        "(No separate staging time published by the organizer -- arrive with "
        "enough buffer to register/pin up/warm up before the start.)",
        "",
        f"Venue: {race.venue}",
        f"Address note: {race.address_source}",
    ]
    if race.notes:
        desc_parts += ["", race.notes]
    desc_parts += [
        "",
        f"Register: {race.register_url}",
        "Results: https://cross-revolution.com/results/",
        "Schedule: https://cross-revolution.com/",
    ]
    desc = "\\n".join(desc_parts)
    lines = [
        "BEGIN:VEVENT",
        f"UID:{race.slug}@cross-revolution.com",
        "DTSTAMP:20260921T000000Z",
        f"DTSTART;TZID={TZID}:{race.date}T{START}",
        f"DTEND;TZID={TZID}:{race.date}T{END}",
        fold(f"SUMMARY:{race.name}"),
        fold(f"LOCATION:{race.location}"),
        fold(f"DESCRIPTION:{desc}"),
        "URL:https://cross-revolution.com/",
        "STATUS:CONFIRMED",
        "BEGIN:VALARM",
        "TRIGGER:-PT1H",
        "ACTION:DISPLAY",
        fold(
            f"DESCRIPTION:Race in 1 hour ({START_LABEL} start -- "
            f"no official staging time published)"
        ),
        "END:VALARM",
        "END:VEVENT",
    ]
    if race.geo:
        lines.insert(7, f"GEO:{race.geo}")
    return "\r\n".join(lines)


def calendar(events: list[str], name: str) -> str:
    return (
        "\r\n".join(
            [
                "BEGIN:VCALENDAR",
                "VERSION:2.0",
                f"PRODID:-//dougch//Cross Revolution 2026//EN",
                "CALSCALE:GREGORIAN",
                "METHOD:PUBLISH",
                fold(f"X-WR-CALNAME:{name}"),
                f"X-WR-TIMEZONE:{TZID}",
                *VTIMEZONE.splitlines(),
                *events,
                "END:VCALENDAR",
            ]
        )
        + "\r\n"
    )


def main() -> None:
    out = Path(__file__).parent
    events = [vevent(r) for r in RACES]
    for race, event in zip(RACES, events):
        (out / f"{race.slug}.ics").write_text(
            calendar([event], race.name)
        )
    (out / "cross-revolution-2026.ics").write_text(
        calendar(events, "Cross Revolution 2026")
    )
    print(f"wrote {len(RACES) + 1} files to {out}")


if __name__ == "__main__":
    main()
