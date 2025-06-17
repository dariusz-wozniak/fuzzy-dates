# Fuzzy Dates

A comprehensive EBNF (Extended Backus-Naur Form) grammar for representing fuzzy, uncertain, and complex temporal expressions. This grammar provides a standardized way to express dates and times with various levels of precision, uncertainty, and contextual information.

## Introduction

The Fuzzy Dates grammar is designed to solve the problem of representing temporal information that is not exact or precise. It's particularly useful in scenarios where:

* Historical records have uncertain dates
* Archaeological findings need temporal context
* Scientific data includes temporal uncertainty
* Business requirements need flexible date ranges
* Cultural or calendar system differences need to be represented

### What is EBNF?

EBNF (Extended Backus-Naur Form) is a notation for formally describing syntax. It's commonly used to define the grammar of programming languages, data formats, and other formal languages. The EBNF file in this repository defines the syntax rules for expressing fuzzy dates in a standardized way.

### How to Use

1. **Parser Implementation**: Use the EBNF grammar to implement a parser in your preferred programming language
2. **Database Storage**: Define database schemas that can store fuzzy date expressions
3. **Testing**: Use the examples provided to test your implementation
4. **Integration**: Integrate the parser into your application for handling fuzzy date inputs

## Features Overview

* Standard Dates — e.g. `1990-05-01`
* Approximate Dates (`~`) — e.g. `~1990`
* Partial Dates (`?`) — e.g. `2025-04-?`
* Time-Only Expressions (`T`) — e.g. `T12:00:00`
* Time-Only Expressions With High Precision — e.g. `2023-11-20T23:59:59.123456789`
* Seasons (`Season-YYYY`) — e.g. `Autumn-2023`
* Periodic Dates (`D`, `W`, `Q`, `H`) — e.g. `D12-2022`
* Centuries (`C`) - e.g. `19C`
* Decades (`YYYYs`) - e.g. `1970s`
* Temporal Qualifiers (`Early-`, `Mid-`, `Late-`) — e.g. `Early-2020`
* Notes and Annotations — e.g. `1985-12-17T08:45:00+02:00#birth of author`
* Geo-Temporal Qualifiers — e.g. `2023-06-15@Tokyo`
* Geo-Temporal Qualifiers With Coordinates — e.g. `2023-06-15T12:00:00@geo:50.061389,19.937222`
* Historical Style Notes — e.g. `1700-03-20(os)`
* Calendar Systems — e.g. `1700-03-20(julian)`
* Ranges and Open-ended Ranges — e.g. `2000..2010`
* Multiple Choices — e.g. `1980-01-01..1981-12-31|1990-01..1992-06`
* Day & Month Choices/Ranges — e.g. `2012-12-[1..3]`
* Uncertainty Expressions — e.g. `2014(±2y)`
* Nested Uncertainty — e.g. `~2023(±1y)(±0.5Q)`
* Ordinal Day-of-Week Expressions — e.g. `1º-Mon-2022`
* Weighted Date Part Choices — e.g. `2020-[03*20%-04*80%]`
* Probability Distributions — e.g. `2023~normal(μ=2023,σ=2)`
* Temporal Integer Choices — e.g. `2023-[03..05]`
* Timezone Handling — e.g. `2024-01-01T00:00:00[America/New_York]`
* Timezone Shifts — e.g. `2024-01-01T00:00:00[EST→EDT]`
* Number Separators — e.g. `1_000_000`

## Detailed Features

### Standard Dates

Basic date expressions in various formats.

Examples:
* `1990`: A specific year
* `2023-05`: A specific year and month
* `2023-05-15`: A specific year, month, and day
* `-449`: Year 449 BC
* `1985-12-17T08:45:00`: Specific date and time (no offset)
* `1985-12-17T08:45:00+02:00`: Specific date and time with a +02:00 timezone offset
* `2024-01-01T00:00:00Z`: January 1, 2024, at midnight UTC
* `2023-10-27T15:30:00PST`: October 27, 2023, 3:30 PM PST
* `2023-11-20T23:59:59.123`: Date and time with milliseconds
* `2023-11-20T23:59:59.123456789`: Date and time with nanoseconds
* `2024-03-08T09:00:00IST`: March 8, 2024, 9:00 AM Indian Standard Time
* `2024-03-08T09:00:00JST`: March 8, 2024, 9:00 AM Japan Standard Time

### Approximate Dates (`~`)

The tilde (`~`) prefix indicates that a date is approximate or estimated.

Examples:
* `~1990`: Approximate year 1990
* `~Autumn-2023`: Approximate year 2023, Autumn season
* `~1944-06-04`: Approximately June 4th, 1944
* `~Late-2020s`: Approximately late 2020s
* `~Early-21C`: Approximately early 21st century
* `~Late-Autumn-2021`: Approximately late Autumn 2021

### Partial Dates (`?`)

Used when only part of a date is known or relevant.

Examples:
* `?-05`: May, unknown year
* `?-?-13`: 13th day of unknown month and year
* `?-05T10:00:00`: May, unknown year, at 10:00:00
* `?-?-13T?:30:00`: 13th day of unknown month and year, at 30 minutes past any hour
* `2021-07-?`: Year 2021, July, any day
* `?-07-?`: Unknown year, July, any day
* `2023-?-15`: 2023, unknown month, 15th day
* `2025-04-?`: April 2025, unknown day

### Time-Only Expressions (`T`)

Expressions that specify only time, without a date.

Examples:
* `T12:00:00`: Any day at noon
* `T?:30:00`: Any hour, at 30 minutes, 00 seconds
* `T?:?:?`: Any time, unknown date
* `T18:00:00`: Any day at 6 PM (18:00)
* `T12:00:00@geo:50.0,20.0`: Noon at specific coordinates
* `T?:?:?@geo:50.0,20.0`: Unknown time, at specific coordinates

### Time-Only Expressions With High Precision

Expressions that include fractional seconds for high precision timing.

Examples:
* `2023-11-20T23:59:59.123`: Date and time with milliseconds
* `2023-11-20T23:59:59.123456789`: Date and time with nanoseconds

### Seasons (`Season-YYYY`)

Representation of seasonal periods.

Examples:
* `Autumn-2023`: A specific season and year
* `Summer-2025`: Another example of season and year
* `~Late-Autumn-2021`: Approximately late Autumn 2021

### Periodic Dates (`D`, `W`, `Q`, `H`)

Special expressions for recurring temporal periods (day of year, week, quarter, half-year).

Examples:
* `D12-2022`: The 12th day of year 2022
* `W12-2022`: Week 12 of year 2022
* `Q2-2023`: Quarter 2 of year 2023
* `H2-2023`: Half-year 2 of year 2023
* `W12-2022-D-1`: Week 12 of 2022, day 1 (Monday)

### Centuries (`C`)

Representation of century periods.

Examples:
* `19C`: Specific 19th Century
* `-5C`: 5th Century BC
* `Early-21C`: Early part of the 21st Century
* `Mid-19C`: Middle of the 19th Century

### Decades (`YYYYs`)

Representation of decade periods.

Examples:
* `1970s`: The decade of the 1970s
* `Early-1970s`: The early part of the 1970s decade
* `~2020s`: Approximately the 2020s decade
* `Late-2020s`: Late part of the 2020s

### Temporal Qualifiers (`Early-`, `Mid-`, `Late-`)

Semantic qualifiers for temporal periods.

Examples:
* `Early-2020`: Early part of 2020
* `Mid-19C`: Middle of the 19th Century
* `Late-2020s`: Late part of the 2020s

### Notes and Annotations

Adding descriptive information to dates.

Examples:
* `1985-12-17T08:45:00+02:00#birth of author`: Specific date and time with timezone and a descriptive note
* `19C#Industrial Revolution`: 19th Century with a descriptive note
* `~Late-2022#ProjectCompletion`: Approximately late 2022, with a note
* `~-13_787_000_000(±20_000_000)#Big Bang`: Approximate point with uncertainty and note
* `~-4_500_000_000#EarthFormation`: Earth's formation with note

### Geo-Temporal Qualifiers

Adding geographical context to temporal expressions.

Examples:
* `2023-06-15@Tokyo`: Date specific to Tokyo timezone
* `1985-12-17T08:45:00@geo:50.061389,19.937222`: Date and time at specific coordinates
* `T12:00:00@geo:34.0522,-118.2437`: Time at specific coordinates

### Historical Style Notes

Representing different calendar systems and historical dating styles.

* `(os)` – Old Style (Julian calendar)
* `(ns)` – New Style (Gregorian calendar)

Examples:
* `1700-03-20(os)`: March 20, 1700, Old Style (Julian calendar)
* `1700-03-20(ns)`: March 20, 1700, New Style (Gregorian calendar)

### Calendar Systems

Explicit specification of calendar systems; use `(calendar)` instead of `(os)` or `(ns)`.

Examples:
* `2023-01-01(iso8601)`: January 1, 2023, ISO 8601 calendar
* `2023-01-01(julian)`: January 1, 2023, Julian calendar
* `2023-01-01(gregorian)`: January 1, 2023, Gregorian calendar
* `100(stardate)`: Year 100, specified with a StarDate calendar

### Ranges and Open-ended Ranges

Expressing periods between two points in time.

Examples:
* `2000..2010`: A year range from 2000 to 2010
* `~1944-06-04..~1944-06-06`: A fuzzy date range
* `19C..20C`: A range of centuries
* `2020-01-01..`: Open-ended range from January 1, 2020 onwards
* `..1990-12-31`: Open-ended range up to December 31, 1990
* `1999s..`: From the 1990s decade onwards
* `~1944-06-04..?`: Start known, end fuzzy
* `?..1945-05-08`: End known, start uncertain
* `?..`: Both start and end uncertain

### Multiple Choices

Expressing alternative temporal possibilities.

Examples:
* `1980-01-01..1981-12-31|1990-01..1992-06`: Multiple date ranges, either 1980-1981 or 1990-1992
* `19C|20C`: Either the 19th Century OR the 20th Century
* `2020|2022`: Either year 2020 or year 2022

### Day & Month Choices/Ranges

Flexible expressions for specific days or months.

Examples:
* `2012-12-[1..3]`: Year 2012, December, between day 1 and day 3 (inclusive)
* `1948-[04-11|05-12|06-01]`: Year 1948, on one of three specific dates
* `2024-06-[5..7]`: June 2024, between the 5th and 7th (inclusive)

### Uncertainty Expressions

Representing uncertainty in temporal expressions.

Examples:
* `2014(±2y)`: Year 2014, with a symmetric uncertainty of ±2 years
* `~2014(+3y-1y)`: Approximately year 2014, with asymmetric uncertainty
* `19C(±1C)`: 19th Century, with an uncertainty of ±1 century
* `2023-05-15T10:00:00(±0.5s)`: May 15, 2023, at 10:00:00, with ±0.5 second uncertainty

### Nested Uncertainty

Expressing multiple layers of uncertainty.

Examples:
* `~2023(±1y)(±0.5Q)`: Nested uncertainty intervals
* `~Early-2020s(±2y)(±1Q)`: Uncertainty in both year and quarter
* `1999-12-31(±1d)(±3h)`: Date with day and hour uncertainty

### Ordinal Day-of-Week Expressions

Expressing specific occurrences of days of the week.

Examples:
* `1º-Mon-2022`: The first Monday of year 2022
* `4º-Fri-Autumn-2023`: The fourth Friday of Autumn 2023
* `[1º..3º]-Mon-H2-2023`: From 1st to 3rd Monday of Half-year 2, 2023

### Weighted Date Part Choices

Expressing probability distributions over date parts.

Examples:
* `2020-[03*20%-04*80%]`: Year 2020, with weighted probability
* `2023-01-[15*60%-16*40%]`: January 2023, with weighted probability
* `[2023*70%-2024*30%]`: Weighted probability for years
* `T[10*30%-11*70%]`: Time with weighted probability

### Probability Distributions

Expressing statistical distributions over temporal periods.

Examples:
* `2023~normal(μ=2023,σ=2)`: Normally distributed around 2023
* `~2024-06-15~uniform(start=2024-06-01,end=2024-06-30)`: Uniform distribution
* `19C~triangular(early=1801,peak=1850,late=1900)`: Triangular distribution

### Temporal Integer Choices

Expressing ranges or choices of temporal integers.

Examples:
* `[2020..2025]`: A range of years from 2020 to 2025
* `2023-[03..05]`: Year 2023, months from March to May
* `2023-01-[10|15|20]`: January 2023, on the 10th, 15th, or 20th
* `T[09..11]:00:00`: Time: any hour between 09 and 11, at 00:00
* `T10:[30|35]:00`: 10 AM, either 30 or 35 minutes, 00 seconds
* `[19C|20C]`: Either the 19th or 20th century

### Timezone Handling

Expressing timezone information.

Examples:
* `2024-01-01T00:00:00[America/New_York]`: Explicit timezone ID
* `2024-01-01T00:00:00Z`: January 1, 2024, at midnight UTC
* `2023-10-27T15:30:00PST`: October 27, 2023, 3:30 PM PST
* `2024-03-08T09:00:00IST`: March 8, 2024, 9:00 AM Indian Standard Time
* `2024-03-08T09:00:00JST`: March 8, 2024, 9:00 AM Japan Standard Time

### Timezone Shifts

Expressing timezone transitions and changes.

Examples:
* `2024-01-01T00:00:00[EST→EDT]`: Timezone with daylight saving shift
* `2024-01-01T00:00:00[UTC+2→UTC+3]`: Timezone offset change

### Number Separators

Using underscores for readability in large numbers.

Examples:
* `1_000_000`: Year 1M
* `-1_234_567_890`: Year -1234567890
* `~-13_787_000_000(±20_000_000)#Big Bang`: Approximate point with uncertainty
* `~-4_500_000_000#EarthFormation`: Earth's formation with readable number
