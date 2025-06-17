### Standard Dates

Basic date expressions in various formats.

**Syntax:**
* `YYYY`: Four-digit year
* `YYYY-MM`: Year and month
* `YYYY-MM-DD`: Full date
* `-YYYY`: Year BC
* `YYYY-MM-DDThh:mm:ss`: Date with time
* `YYYY-MM-DDThh:mm:ss±hh:mm`: Date with timezone offset
* `YYYY-MM-DDThh:mm:ssZ`: UTC time
* `YYYY-MM-DDThh:mm:ss[ZoneID]`: Date with IANA timezone ID
* `YYYY-MM-DDThh:mm:ss[Zone]`: Date with timezone abbreviation
* `YYYY-MM-DDThh:mm:ss.sss`: Date with fractional seconds
* `YYYY-MM-DDThh:mm:ss.sssssssss`: Date with nanosecond precision

Where:
* `ZoneID` is an IANA timezone identifier (e.g., `America/New_York`)
* `Zone` is a timezone abbreviation (e.g., `PST`, `IST`, `JST`)
* `sss` represents any number of decimal places for fractional seconds

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

**Syntax:**
* `~YYYY`: Approximate year
* `~YYYY-MM`: Approximate month
* `~YYYY-MM-DD`: Approximate day
* `~Season-YYYY`: Approximate season
* `~TemporalQualifier-Period`: Approximate period with qualifier

Examples:
* `~1990`: Approximate year 1990
* `~Autumn-2023`: Approximate year 2023, Autumn season
* `~1944-06-04`: Approximately June 4th, 1944
* `~Late-2020s`: Approximately late 2020s
* `~Early-21C`: Approximately early 21st century
* `~Late-Autumn-2021`: Approximately late Autumn 2021

### Partial Dates (`?`)

Used when only part of a date is known or relevant.

**Syntax:**
* `?-MM`: Known month, unknown year
* `?-?-DD`: Known day, unknown month and year
* `YYYY-MM-?`: Known year and month, unknown day
* `YYYY-?-DD`: Known year and day, unknown month
* `?-MM-DD`: Known month and day, unknown year

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

**Syntax:**
* `Thh:mm:ss`: Full time
* `Thh:mm`: Hours and minutes
* `T?:mm:ss`: Unknown hour
* `Thh:?:ss`: Unknown minutes
* `Thh:mm:?`: Unknown seconds
* `T?:?:?`: Completely unknown time

Examples:
* `T12:00:00`: Any day at noon
* `T?:30:00`: Any hour, at 30 minutes, 00 seconds
* `T?:?:?`: Any time, unknown date
* `T18:00:00`: Any day at 6 PM (18:00)
* `T12:00:00@geo:50.0,20.0`: Noon at specific coordinates
* `T?:?:?@geo:50.0,20.0`: Unknown time, at specific coordinates

### Time-Only Expressions With High Precision

Expressions that include fractional seconds for high precision timing.

**Syntax:**
* `Thh:mm:ss.sss`: Time with fractional seconds
* `Thh:mm:ss.sssssssss`: Time with nanosecond precision
* `YYYY-MM-DDThh:mm:ss.sss`: Date and time with fractional seconds
* `YYYY-MM-DDThh:mm:ss.sssssssss`: Date and time with nanosecond precision

Where:
* `sss` represents any number of decimal places for fractional seconds
* Precision is not limited to milliseconds or nanoseconds, but can be any number of decimal places

Examples:
* `2023-11-20T23:59:59.123`: Date and time with milliseconds
* `2023-11-20T23:59:59.123456789`: Date and time with nanoseconds

### Seasons (`Season-YYYY`)

Representation of seasonal periods.

**Syntax:**
* `Season-YYYY`: Specific season in a year
* `~Season-YYYY`: Approximate season
* `TemporalQualifier-Season-YYYY`: Qualified season

Where `Season` is one of: `Spring`, `Summer`, `Autumn`, `Winter`

Examples:
* `Autumn-2023`: A specific season and year
* `Summer-2025`: Another example of season and year
* `~Late-Autumn-2021`: Approximately late Autumn 2021

### Periodic Dates (`D`, `W`, `Q`, `H`)

Special expressions for recurring temporal periods (day of year, week, quarter, half-year).

**Syntax:**
* `Dddd-YYYY`: Day of year (1-366)
* `Www-YYYY`: Week of year (1-53)
* `Qq-YYYY`: Quarter of year (1-4)
* `Hh-YYYY`: Half of year (1-2)
* `Www-YYYY-D-d`: Week and day of week (1-7)

Examples:
* `D12-2022`: The 12th day of year 2022
* `W12-2022`: Week 12 of year 2022
* `Q2-2023`: Quarter 2 of year 2023
* `H2-2023`: Half-year 2 of year 2023
* `W12-2022-D-1`: Week 12 of 2022, day 1 (Monday)

### Centuries (`C`)

Representation of century periods.

**Syntax:**
* `nC`: nth century AD
* `-nC`: nth century BC
* `TemporalQualifier-nC`: Qualified century
* `~nC`: Approximate century

Where `n` is a positive integer

Examples:
* `19C`: Specific 19th Century
* `-5C`: 5th Century BC
* `Early-21C`: Early part of the 21st Century
* `Mid-19C`: Middle of the 19th Century

### Decades (`YYYYs`)

Representation of decade periods.

**Syntax:**
* `YYYYs`: Decade starting with YYYY
* `TemporalQualifier-YYYYs`: Qualified decade
* `~YYYYs`: Approximate decade

Where `YYYY` is a year ending in 0

Examples:
* `1970s`: The decade of the 1970s
* `Early-1970s`: The early part of the 1970s decade
* `~2020s`: Approximately the 2020s decade
* `Late-2020s`: Late part of the 2020s

### Temporal Qualifiers (`Early-`, `Mid-`, `Late-`)

Semantic qualifiers for temporal periods.

**Syntax:**
* `Early-Period`: Early part of a period
* `Mid-Period`: Middle part of a period
* `Late-Period`: Late part of a period

Where `Period` can be a year, decade, century, season, or other temporal unit

Examples:
* `Early-2020`: Early part of 2020
* `Mid-19C`: Middle of the 19th Century
* `Late-2020s`: Late part of the 2020s

### Notes and Annotations

Adding descriptive information to dates.

**Syntax:**
* `Date#Note`: Date with a note
* `Date(Uncertainty)#Note`: Date with uncertainty and note
* `Date@Location#Note`: Date with location and note

Where `Note` is any text describing the date's significance

Examples:
* `1985-12-17T08:45:00+02:00#birth of author`: Specific date and time with timezone and a descriptive note
* `19C#Industrial Revolution`: 19th Century with a descriptive note
* `~Late-2022#ProjectCompletion`: Approximately late 2022, with a note
* `~-13_787_000_000(±20_000_000)#Big Bang`: Approximate point with uncertainty and note
* `~-4_500_000_000#EarthFormation`: Earth's formation with note

### Geo-Temporal Qualifiers

Adding geographical context to temporal expressions.

**Syntax:**
* `Date@Location`: Date with location name
* `Date@geo:lat,lon`: Date with coordinates
* `Time@Location`: Time with location
* `Time@geo:lat,lon`: Time with coordinates

Examples:
* `2023-06-15@Tokyo`: Date specific to Tokyo timezone
* `1985-12-17T08:45:00@geo:50.061389,19.937222`: Date and time at specific coordinates
* `T12:00:00@geo:34.0522,-118.2437`: Time at specific coordinates

### Historical Style Notes

Representing different calendar systems and historical dating styles.

**Syntax:**
* `Date(os)`: Old Style (Julian calendar)
* `Date(ns)`: New Style (Gregorian calendar)

Examples:
* `1700-03-20(os)`: March 20, 1700, Old Style (Julian calendar)
* `1700-03-20(ns)`: March 20, 1700, New Style (Gregorian calendar)

### Calendar Systems

Explicit specification of calendar systems; use `(calendar)` instead of `(os)` or `(ns)`.

**Syntax:**
* `Date(calendar)`: Date in specific calendar system
* `Date(iso8601)`: ISO 8601 calendar
* `Date(julian)`: Julian calendar
* `Date(gregorian)`: Gregorian calendar
* `Date(custom)`: Custom calendar system

Examples:
* `2023-01-01(iso8601)`: January 1, 2023, ISO 8601 calendar
* `2023-01-01(julian)`: January 1, 2023, Julian calendar
* `2023-01-01(gregorian)`: January 1, 2023, Gregorian calendar
* `100(stardate)`: Year 100, specified with a StarDate calendar

### Ranges and Open-ended Ranges

Expressing periods between two points in time.

**Syntax:**
* `Start..End`: Range from Start to End
* `Start..`: Open-ended range from Start
* `..End`: Open-ended range until End
* `?..End`: Uncertain start, known end
* `Start..?`: Known start, uncertain end
* `?..`: Completely uncertain range

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

**Syntax:**
* `Option1|Option2`: Either Option1 or Option2
* `Range1|Range2`: Either Range1 or Range2
* `Date1|Date2|Date3`: One of multiple dates

Examples:
* `1980-01-01..1981-12-31|1990-01..1992-06`: Multiple date ranges, either 1980-1981 or 1990-1992
* `19C|20C`: Either the 19th Century OR the 20th Century
* `2020|2022`: Either year 2020 or year 2022

### Day & Month Choices/Ranges

Flexible expressions for specific days or months.

**Syntax:**
* `YYYY-MM-[D1..D2]`: Range of days in a month
* `YYYY-[M1-D1|M2-D2]`: Specific dates in a year
* `YYYY-MM-[D1|D2|D3]`: Multiple days in a month

Examples:
* `2012-12-[1..3]`: Year 2012, December, between day 1 and day 3 (inclusive)
* `1948-[04-11|05-12|06-01]`: Year 1948, on one of three specific dates
* `2024-06-[5..7]`: June 2024, between the 5th and 7th (inclusive)

### Uncertainty Expressions

Representing uncertainty in temporal expressions.

**Syntax:**
* `Date(±Nunit)`: Symmetric uncertainty
* `Date(+Nunit-Munit)`: Asymmetric uncertainty
* `~Date(±Nunit)`: Approximate date with uncertainty

Where `unit` can be: `y` (year), `Q` (quarter), `m` (month), `d` (day), `h` (hour), `min` (minute), `s` (second)

Examples:
* `2014(±2y)`: Year 2014, with a symmetric uncertainty of ±2 years
* `~2014(+3y-1y)`: Approximately year 2014, with asymmetric uncertainty
* `19C(±1C)`: 19th Century, with an uncertainty of ±1 century
* `2023-05-15T10:00:00(±0.5s)`: May 15, 2023, at 10:00:00, with ±0.5 second uncertainty

### Nested Uncertainty

Expressing multiple layers of uncertainty.

**Syntax:**
* `Date(Uncertainty1)(Uncertainty2)`: Multiple uncertainty levels
* `~Date(Uncertainty1)(Uncertainty2)`: Approximate date with multiple uncertainties

Examples:
* `~2023(±1y)(±0.5Q)`: Nested uncertainty intervals
* `~Early-2020s(±2y)(±1Q)`: Uncertainty in both year and quarter
* `1999-12-31(±1d)(±3h)`: Date with day and hour uncertainty

### Ordinal Day-of-Week Expressions

Expressing specific occurrences of days of the week.

**Syntax:**
* `nº-Day-Period`: nth occurrence of a day in a period
* `[nº..mº]-Day-Period`: Range of occurrences
* `nº-Day-Season-YYYY`: Specific occurrence in a season

Where `Day` is: `Mon`, `Tue`, `Wed`, `Thu`, `Fri`, `Sat`, `Sun`

Examples:
* `1º-Mon-2022`: The first Monday of year 2022
* `4º-Fri-Autumn-2023`: The fourth Friday of Autumn 2023
* `[1º..3º]-Mon-H2-2023`: From 1st to 3rd Monday of Half-year 2, 2023

### Weighted Date Part Choices

Expressing probability distributions over date parts.

**Syntax:**
* `[Part1*P1%-Part2*P2%]`: Weighted choice between parts
* `[Year*P1%-Year*P2%]`: Weighted year choice
* `[Month*P1%-Month*P2%]`: Weighted month choice

Where `P1`, `P2` are percentages that sum to 100%

Examples:
* `2020-[03*20%-04*80%]`: Year 2020, with weighted probability
* `2023-01-[15*60%-16*40%]`: January 2023, with weighted probability
* `[2023*70%-2024*30%]`: Weighted probability for years
* `T[10*30%-11*70%]`: Time with weighted probability

### Probability Distributions

Expressing statistical distributions over temporal periods.

**Syntax:**
* `Date~normal(μ=value,σ=value)`: Normal distribution
* `Date~uniform(start=date,end=date)`: Uniform distribution
* `Date~triangular(early=date,peak=date,late=date)`: Triangular distribution

Examples:
* `2023~normal(μ=2023,σ=2)`: Normally distributed around 2023
* `~2024-06-15~uniform(start=2024-06-01,end=2024-06-30)`: Uniform distribution
* `19C~triangular(early=1801,peak=1850,late=1900)`: Triangular distribution

### Temporal Integer Choices

Expressing ranges or choices of temporal integers.

**Syntax:**
* `[N..M]`: Range of integers
* `[N|M|P]`: Choice of integers
* `YYYY-[MM..MM]`: Range of months
* `YYYY-MM-[DD..DD]`: Range of days

Examples:
* `[2020..2025]`: A range of years from 2020 to 2025
* `2023-[03..05]`: Year 2023, months from March to May
* `2023-01-[10|15|20]`: January 2023, on the 10th, 15th, or 20th
* `T[09..11]:00:00`: Time: any hour between 09 and 11, at 00:00
* `T10:[30|35]:00`: 10 AM, either 30 or 35 minutes, 00 seconds
* `[19C|20C]`: Either the 19th or 20th century

### Timezone Handling

Expressing timezone information.

**Syntax:**
* `DateTTime[Zone]`: Date and time in specific timezone
* `DateTTimeZ`: UTC time
* `DateTTime±hh:mm`: Timezone offset
* `DateTTime[ZoneID]`: IANA timezone ID
* `DateTTime[Zone]`: Timezone abbreviation

Where:
* `ZoneID` is an IANA timezone identifier (e.g., `America/New_York`)
* `Zone` is a timezone abbreviation (e.g., `PST`, `IST`, `JST`, `UTC`)

Examples:
* `2024-01-01T00:00:00[America/New_York]`: Explicit timezone ID
* `2024-01-01T00:00:00Z`: January 1, 2024, at midnight UTC
* `2023-10-27T15:30:00PST`: October 27, 2023, 3:30 PM PST
* `2024-03-08T09:00:00IST`: March 8, 2024, 9:00 AM Indian Standard Time
* `2024-03-08T09:00:00JST`: March 8, 2024, 9:00 AM Japan Standard Time

### Timezone Shifts

Expressing timezone transitions and changes.

**Syntax:**
* `DateTTime[Zone1→Zone2]`: Timezone transition
* `DateTTime[Offset1→Offset2]`: Offset change

Examples:
* `2024-01-01T00:00:00[EST→EDT]`: Timezone with daylight saving shift
* `2024-01-01T00:00:00[UTC+2→UTC+3]`: Timezone offset change

### Number Separators

Using underscores for readability in large numbers.

**Syntax:**
* `n_nnn_nnn`: Number with underscore separators
* `-n_nnn_nnn`: Negative number with separators
* `~n_nnn_nnn`: Approximate number with separators

Examples:
* `1_000_000`: Year 1M
* `-1_234_567_890`: Year -1234567890
* `~-13_787_000_000(±20_000_000)#Big Bang`: Approximate point with uncertainty
* `~-4_500_000_000#EarthFormation`: Earth's formation with readable number