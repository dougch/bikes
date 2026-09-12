#!/usr/bin/env python3
"""Generate .ics files for the 2026 MFG Cyclocross series, Cat 4 Male 50+ wave.

Source: https://mfgcyclocross.bike/ (race pages + /series-info/)
Third wave of the day: staging 10:35 AM, start 10:50 AM, 40 min race.
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
    podium: str
    notes: str


RACES: list[Race] = [
    Race(
        slug="01-beach-party-silver-lake",
        name="MFG CX #1 - Beach Party at Silver Lake",
        date="20260913",
        venue="Thornton A. Sullivan Park (Silver Lake)",
        location="Thornton A. Sullivan Park, 11405 Silver Lake Rd, Everett, WA 98208",
        geo="47.889414;-122.211069",
        address_source="street address not on race page; coords from race page",
        podium="12:00 PM",
        notes=(
            "Racer parking at the northwest end of the park. Team tent access road "
            "closes at 8:15 AM; cars near start/finish are stuck until 3:45 PM. "
            "No alcohol at this venue."
        ),
    ),
    Race(
        slug="02-north-40-lemay",
        name="MFG CX #2 - North 40 at LeMay",
        date="20260927",
        venue="LeMay Car Collection - North 40",
        location="14601 4th Ave E, Tacoma, WA 98445",
        geo="",
        address_source="street address published on race page",
        podium="12:00 PM",
        notes=(
            "Gravel/grass parking on the north and northwest sides; tight, carpool. "
            "Approach passes through a residential area and an apparent private "
            "drive - keep going. Infield tents up by 8:30 AM, down after 3:45 PM."
        ),
    ),
    Race(
        slug="03-barnburner-steilacoom",
        name="MFG CX #3 - Barnburner at Steilacoom",
        date="20261011",
        venue="Fort Steilacoom Park",
        location="Fort Steilacoom Park, 8714 87th Ave SW, Lakewood, WA 98498",
        geo="47.1720871;-122.5626644",
        address_source="street address not on race page; coords from race page",
        podium="12:00 PM",
        notes=(
            "Ample parking in the grass field and dedicated lots on the way in. "
            "Roughly an hour south of Seattle."
        ),
    ),
    Race(
        slug="04-magnuson-park-cross",
        name="MFG CX #4 - Magnuson Park Cross",
        date="20261025",
        venue="Magnuson Park",
        location="Magnuson Park, 7400 Sand Point Way NE, Seattle, WA 98115",
        geo="47.676796;-122.250351",
        address_source="street address not on race page; coords from race page",
        podium="12:00 PM",
        notes=(
            "Park in E1 or E5. Lot E4 is closest but closes at 8:30 AM and does not "
            "release until ~4 PM. No parking on the road or in E3. Stay on pavement - "
            "no riding through the wetlands or on Kite Hill."
        ),
    ),
    Race(
        slug="05-pumpkin-smash-swans-trail",
        name="MFG CX #5 - Pumpkin Smash CX at Swans Trail Farms",
        date="20261108",
        venue="Swans Trail Farms",
        location="7301 Rivershore Rd, Snohomish, WA 98290",
        geo="",
        address_source="street address published on race page",
        podium="12:00 PM",
        notes=(
            "Parking in the grass field on the north end; follow MFG signs. No "
            "vehicle access to the team tent field. Working farm - bring boots. "
            "Barn area is taped off."
        ),
    ),
    Race(
        slug="06-woodland-park-gp",
        name="MFG CX #6 - Woodland Park Gran Prix",
        date="20261122",
        venue="Woodland Park",
        location="Woodland Park, 1000 N 50th St, Seattle, WA 98103",
        geo="47.66489;-122.34487",
        address_source="street address not on race page; coords from race page",
        podium="1:15 PM",
        notes=(
            "Lot at the southwest corner, west of registration, is best but fills "
            "early. Neighborhood streets and other park lots also work. Loop road is "
            "gear drop-off only, before 8:30 AM or after 4 PM."
        ),
    ),
]

CATEGORY = "Cat 4 Male 50+"
CATEGORY_SLUG = "cat4-50plus"
STAGING = "103500"
START = "105000"
END = "113000"  # 10:50 start + 40 min race
STAGING_LABEL = "10:35 AM"
START_LABEL = "10:50 AM"
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
    desc = (
        f"Category: {CATEGORY}\\n"
        f"Staging: {STAGING_LABEL}\\nStart: {START_LABEL}\\n"
        f"Race length: {DURATION_LABEL}\\n"
        f"Podium: {race.podium}\\n\\n"
        f"Venue: {race.venue}\\n"
        f"Address note: {race.address_source}\\n\\n"
        f"{race.notes}\\n\\n"
        f"Register/results: https://www.webscorer.com/mfgcyclocross\\n"
        f"Schedule: https://mfgcyclocross.bike/series-info/"
    )
    lines = [
        "BEGIN:VEVENT",
        f"UID:{race.slug}-{CATEGORY_SLUG}@mfgcyclocross.bike",
        "DTSTAMP:20260909T000000Z",
        f"DTSTART;TZID={TZID}:{race.date}T{STAGING}",
        f"DTEND;TZID={TZID}:{race.date}T{END}",
        fold(f"SUMMARY:{race.name} - {CATEGORY}"),
        fold(f"LOCATION:{race.location}"),
        fold(f"DESCRIPTION:{desc}"),
        "URL:https://mfgcyclocross.bike/",
        "STATUS:CONFIRMED",
        "BEGIN:VALARM",
        "TRIGGER:-PT1H",
        "ACTION:DISPLAY",
        f"DESCRIPTION:{CATEGORY} staging in 1 hour ({STAGING_LABEL})",
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
                f"PRODID:-//dougch//MFG CX 2026 {CATEGORY}//EN",
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
            calendar([event], f"{race.name} - {CATEGORY}")
        )
    (out / f"mfg-cx-2026-{CATEGORY_SLUG}.ics").write_text(
        calendar(events, f"MFG Cyclocross 2026 - {CATEGORY}")
    )
    print(f"wrote {len(RACES) + 1} files to {out}")


if __name__ == "__main__":
    main()
