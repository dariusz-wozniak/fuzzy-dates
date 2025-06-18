[Version: 2025-06-17_1](versions.md)

**fuzzy_date_expression:**

![fuzzy_date_expression](syntax/fuzzy_date_expression.png)

```
fuzzy_date_expression
         ::= temporal_expression_unit ( '|' temporal_expression_unit )*
```

**temporal_expression_unit:**

![temporal_expression_unit](syntax/temporal_expression_unit.png)

```
temporal_expression_unit
         ::= date_expr
           | time_only_expr
           | century_expr
           | decade_expr
           | numeric_timeline_point
           | day_of_year_expr
           | week_expr
           | quarter_expr
           | half_year_expr
           | ordinal_day_expr
           | range_expr
           | partial_date_expr
```

referenced by:

* fuzzy_date_expression

**range_expr:**

![range_expr](syntax/range_expr.png)

```
range_expr
         ::= temporal_expression_boundary '..' temporal_expression_boundary
```

referenced by:

* temporal_expression_unit

**temporal_expression_boundary:**

![temporal_expression_boundary](syntax/temporal_expression_boundary.png)

```
temporal_expression_boundary
         ::= date_expr
           | century_expr
           | decade_expr
           | day_of_year_expr
           | week_expr
           | quarter_expr
           | half_year_expr
           | ordinal_day_expr
           | ''
           | '?'
```

referenced by:

* range_expr

**temporal_qualifier:**

![temporal_qualifier](syntax/temporal_qualifier.png)

```
temporal_qualifier
         ::= 'Early'
           | 'Mid'
           | 'Late'
```

**uncertainty:**

![uncertainty](syntax/uncertainty.png)

```
uncertainty
         ::= '(' uncertainty_content ')'
```

**uncertainty_content:**

![uncertainty_content](syntax/uncertainty_content.png)

```
uncertainty_content
         ::= uncertainty_symmetric
           | uncertainty_asymmetric
           | distribution_details
```

referenced by:

* uncertainty

**uncertainty_symmetric:**

![uncertainty_symmetric](syntax/uncertainty_symmetric.png)

```
uncertainty_symmetric
         ::= '±' number [uncertaiy_]
```

referenced by:

* uncertainty_content

**uncertainty_asymmetric:**

![uncertainty_asymmetric](syntax/uncertainty_asymmetric.png)

```
uncertainty_asymmetric
         ::= '+' number [uncertaiy_] '-' number [uncertaiy_]
```

referenced by:

* uncertainty_content

**uncertainty_unit:**

![uncertainty_unit](syntax/uncertainty_unit.png)

```
uncertainty_unit
         ::= 'y'
           | 'Q'
           | 'm'
           | 'd'
           | 'h'
           | 'min'
           | 's'
```

**distribution_details:**

![distribution_details](syntax/distribution_details.png)

```
distribution_details
         ::= distribution_name '(' distribution_param_list ')'
```

referenced by:

* uncertainty_content

**distribution_name:**

![distribution_name](syntax/distribution_name.png)

```
distribution_name
         ::= 'normal'
           | 'uniform'
           | 'triangular'
```

referenced by:

* distribution_details

**distribution_param_list:**

![distribution_param_list](syntax/distribution_param_list.png)

```
distribution_param_list
         ::= distribution_param ( ',' distribution_param )*
```

referenced by:

* distribution_details

**distribution_param:**

![distribution_param](syntax/distribution_param.png)

```
distribution_param
         ::= label '=' ( number | date_expr )
```

referenced by:

* distribution_param_list

**label:**

![label](syntax/label.png)

```
label    ::= ( letter | digit | '_' )+
```

referenced by:

* distribution_param

**date_expr:**

![date_expr](syntax/date_expr.png)

```
date_expr
         ::= [ '~] [ temporal_quif'-'] date_prefix [uncertaiy]* [ time_copn] [ timezon_cp] [ geo_qualifr] [ note_cmp] [ style_no] [
                  calendr_sytm]
```

referenced by:

* distribution_param
* temporal_expression_boundary
* temporal_expression_unit

**partial_date_expr:**

![partial_date_expr](syntax/partial_date_expr.png)

```
partial_date_expr
         ::= '?' '-' ( month_component | '?' '-' day_component ) [ time_copn] [ geo_qualifr] [ note_cmp] [ style_no] [ calendr_sytm]
```

referenced by:

* temporal_expression_unit

**date_prefix:**

![date_prefix](syntax/date_prefix.png)

```
date_prefix
         ::= year [ '-'month_cpe] [ '-'day_compnet]
           | season_name '-' year
```

referenced by:

* date_expr
* ordinal_temporal_period_reference

**season_name:**

![season_name](syntax/season_name.png)

```
season_name
         ::= 'Spring'
           | 'Summer'
           | 'Autumn'
           | 'Winter'
```

referenced by:

* date_prefix

**century_expr:**

![century_expr](syntax/century_expr.png)

```
century_expr
         ::= [ '~] [ temporal_quif'-'] century_number 'C' [uncertaiy]* [ style_no] [ calendr_sytm]
```

referenced by:

* ordinal_temporal_period_reference
* temporal_expression_boundary
* temporal_expression_unit

**century_number:**

![century_number](syntax/century_number.png)

```
century_number
         ::= integer_number
           | temporal_integer_choice
```

referenced by:

* century_expr

**decade_expr:**

![decade_expr](syntax/decade_expr.png)

```
decade_expr
         ::= [ '~] [ temporal_quif'-'] decade_number 's' [uncertaiy]* [ style_no] [ calendr_sytm]
```

referenced by:

* ordinal_temporal_period_reference
* temporal_expression_boundary
* temporal_expression_unit

**decade_number:**

![decade_number](syntax/decade_number.png)

```
decade_number
         ::= digit digit digit
```

referenced by:

* decade_expr

**day_of_year_expr:**

![day_of_year_expr](syntax/day_of_year_expr.png)

```
day_of_year_expr
         ::= [ '~] 'D' day_number_in_year '-' year [uncertaiy]* [ note_cmp] [ style_no] [ calendr_sytm]
```

referenced by:

* temporal_expression_boundary
* temporal_expression_unit

**day_number_in_year:**

![day_number_in_year](syntax/day_number_in_year.png)

```
day_number_in_year
         ::= digit [ digt] [ digt]
```

referenced by:

* day_of_year_expr

**week_expr:**

![week_expr](syntax/week_expr.png)

```
week_expr
         ::= [ '~] [ temporal_quif'-'] 'W' digit digit '-' year [ '-''D-'day_ofweknumbrpic] [uncertaiy]* [ note_cmp] [ style_no] [ calendr_sytm]
```

referenced by:

* ordinal_temporal_period_reference
* temporal_expression_boundary
* temporal_expression_unit

**quarter_expr:**

![quarter_expr](syntax/quarter_expr.png)

```
quarter_expr
         ::= [ '~] [ temporal_quif'-'] 'Q' ( '1' | '2' | '3' | '4' ) '-' year [uncertaiy]* [ note_cmp] [ style_no] [ calendr_sytm]
```

referenced by:

* ordinal_temporal_period_reference
* temporal_expression_boundary
* temporal_expression_unit

**half_year_expr:**

![half_year_expr](syntax/half_year_expr.png)

```
half_year_expr
         ::= [ '~] [ temporal_quif'-'] 'H' ( '1' | '2' ) '-' year [uncertaiy]* [ note_cmp] [ style_no] [ calendr_sytm]
```

referenced by:

* ordinal_temporal_period_reference
* temporal_expression_boundary
* temporal_expression_unit

**ordinal_day_expr:**

![ordinal_day_expr](syntax/ordinal_day_expr.png)

```
ordinal_day_expr
         ::= [ '~] ( ordinal_day_single | ordinal_day_range ) [uncertaiy]* [ note_cmp] [ style_no] [ calendr_sytm]
```

referenced by:

* temporal_expression_boundary
* temporal_expression_unit

**ordinal_day_single:**

![ordinal_day_single](syntax/ordinal_day_single.png)

```
ordinal_day_single
         ::= ordinal_number '-' day_of_week_short '-' ordinal_temporal_period_reference
```

referenced by:

* ordinal_day_expr

**ordinal_day_range:**

![ordinal_day_range](syntax/ordinal_day_range.png)

```
ordinal_day_range
         ::= '[' ordinal_number '..' ordinal_number ']' '-' day_of_week_short '-' ordinal_temporal_period_reference
```

referenced by:

* ordinal_day_expr

**ordinal_number:**

![ordinal_number](syntax/ordinal_number.png)

```
ordinal_number
         ::= digit+ 'º'
```

referenced by:

* ordinal_day_range
* ordinal_day_single

**day_of_week_short:**

![day_of_week_short](syntax/day_of_week_short.png)

```
day_of_week_short
         ::= 'Mon'
           | 'Tue'
           | 'Wed'
           | 'Thu'
           | 'Fri'
           | 'Sat'
           | 'Sun'
```

referenced by:

* ordinal_day_range
* ordinal_day_single

**day_of_week_number_periodic:**

![day_of_week_number_periodic](syntax/day_of_week_number_periodic.png)

```
day_of_week_number_periodic
         ::= '1'
           | '2'
           | '3'
           | '4'
           | '5'
           | '6'
           | '7'
```

**ordinal_temporal_period_reference:**

![ordinal_temporal_period_reference](syntax/ordinal_temporal_period_reference.png)

```
ordinal_temporal_period_reference
         ::= year
           | date_prefix
           | decade_expr
           | century_expr
           | week_expr
           | quarter_expr
           | half_year_expr
```

referenced by:

* ordinal_day_range
* ordinal_day_single

**numeric_timeline_point:**

![numeric_timeline_point](syntax/numeric_timeline_point.png)

```
numeric_timeline_point
         ::= [ '~] number [uncertaiy]* [ note_cmp]
```

referenced by:

* temporal_expression_unit

**time_only_expr:**

![time_only_expr](syntax/time_only_expr.png)

```
time_only_expr
         ::= 'T' time_component [ timezon_cp] [ geo_qualifr] [ note_cmp] [ style_no] [ calendr_sytm]
```

referenced by:

* temporal_expression_unit

**geo_qualifier:**

![geo_qualifier](syntax/geo_qualifier.png)

```
geo_qualifier
         ::= '@' ( location_name | geo_coordinates )
```

**location_name:**

![location_name](syntax/location_name.png)

```
location_name
         ::= character_in_location_name+
```

referenced by:

* geo_qualifier

**character_in_location_name:**

![character_in_location_name](syntax/character_in_location_name.png)

```
character_in_location_name
         ::= letter
           | digit
           | ' '
           | '/'
           | '-'
           | '_'
```

referenced by:

* location_name

**geo_coordinates:**

![geo_coordinates](syntax/geo_coordinates.png)

```
geo_coordinates
         ::= 'geo:' number ',' number
```

referenced by:

* geo_qualifier

**weighted_date_part:**

![weighted_date_part](syntax/weighted_date_part.png)

```
weighted_date_part
         ::= ( year | month_number_literal | day_number_literal | century_number_literal | hour_literal | minute_literal | second_literal ) '*' percentage
```

referenced by:

* weighted_date_part_choice

**weighted_date_part_choice:**

![weighted_date_part_choice](syntax/weighted_date_part_choice.png)

```
weighted_date_part_choice
         ::= '[' weighted_date_part ( '-' weighted_date_part )* ']'
```

referenced by:

* day_component
* hour_component
* minute_component
* month_component
* second_component

**temporal_integer_choice:**

![temporal_integer_choice](syntax/temporal_integer_choice.png)

```
temporal_integer_choice
         ::= '[' ( integer_range | integer_discrete ) ']'
```

referenced by:

* century_number
* day_component
* hour_component
* minute_component
* month_component
* second_component
* year

**integer_range:**

![integer_range](syntax/integer_range.png)

```
integer_range
         ::= integer_number '..' integer_number
```

referenced by:

* temporal_integer_choice

**integer_discrete:**

![integer_discrete](syntax/integer_discrete.png)

```
integer_discrete
         ::= integer_number ( '|' integer_number )*
```

referenced by:

* temporal_integer_choice

**month_number_literal:**

![month_number_literal](syntax/month_number_literal.png)

```
month_number_literal
         ::= '0' ( '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' )
           | '1' ( '0' | '1' | '2' )
```

referenced by:

* date_pair
* month_component
* weighted_date_part

**month_component:**

![month_component](syntax/month_component.png)

```
month_component
         ::= month_number_literal
           | '?'
           | weighted_date_part_choice
           | multi_date_choice
           | temporal_integer_choice
```

referenced by:

* partial_date_expr

**day_number_literal:**

![day_number_literal](syntax/day_number_literal.png)

```
day_number_literal
         ::= '0' ( '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' )
           | ( '1' | '2' ) digit
           | '3' ( '0' | '1' )
```

referenced by:

* date_pair
* day_component
* day_number_or_wildcard
* day_range
* weighted_date_part

**day_component:**

![day_component](syntax/day_component.png)

```
day_component
         ::= day_number_literal
           | '?'
           | day_choice_component
           | weighted_date_part_choice
           | temporal_integer_choice
```

referenced by:

* partial_date_expr

**time_component:**

![time_component](syntax/time_component.png)

```
time_component
         ::= hour_component ':' minute_component [ ':second_mptfrail]
```

referenced by:

* time_only_expr

**fractional_seconds_opt:**

![fractional_seconds_opt](syntax/fractional_seconds_opt.png)

```
fractional_seconds_opt
         ::= [ fractionl_sed]
```

**hour_literal:**

![hour_literal](syntax/hour_literal.png)

```
hour_literal
         ::= ( '0' | '1' ) digit
           | '2' ( '0' | '1' | '2' | '3' )
```

referenced by:

* hour_component
* weighted_date_part

**hour_component:**

![hour_component](syntax/hour_component.png)

```
hour_component
         ::= hour_literal
           | '?'
           | weighted_date_part_choice
           | temporal_integer_choice
```

referenced by:

* time_component

**minute_literal:**

![minute_literal](syntax/minute_literal.png)

```
minute_literal
         ::= ( '0' | '1' | '2' ( '3' | '4' | '5' ) ) digit
```

referenced by:

* minute_component
* weighted_date_part

**minute_component:**

![minute_component](syntax/minute_component.png)

```
minute_component
         ::= minute_literal
           | '?'
           | weighted_date_part_choice
           | temporal_integer_choice
```

referenced by:

* time_component

**second_literal:**

![second_literal](syntax/second_literal.png)

```
second_literal
         ::= ( '0' | '1' | '2' ( '3' | '4' | '5' ) ) digit
```

referenced by:

* second_component
* weighted_date_part

**second_component:**

![second_component](syntax/second_component.png)

```
second_component
         ::= second_literal
           | '?'
           | weighted_date_part_choice
           | temporal_integer_choice
```

**fractional_seconds:**

![fractional_seconds](syntax/fractional_seconds.png)

```
fractional_seconds
         ::= '.' digit+
```

**timezone_component:**

![timezone_component](syntax/timezone_component.png)

```
timezone_component
         ::= 'Z'
           | ( '+' | '-' ) tz_hour ':' tz_minute
           | letter letter letter
           | '[' ( timezone_full_id | timezone_transition ) ']'
```

**timezone_full_id:**

![timezone_full_id](syntax/timezone_full_id.png)

```
timezone_full_id
         ::= character_in_timezone_id+
```

referenced by:

* timezone_component
* timezone_transition

**character_in_timezone_id:**

![character_in_timezone_id](syntax/character_in_timezone_id.png)

```
character_in_timezone_id
         ::= letter
           | digit
           | '_'
           | '/'
           | '+'
           | '-'
```

referenced by:

* timezone_full_id

**timezone_transition:**

![timezone_transition](syntax/timezone_transition.png)

```
timezone_transition
         ::= timezone_full_id '→' timezone_full_id
```

referenced by:

* timezone_component

**note_component:**

![note_component](syntax/note_component.png)

```
note_component
         ::= '#' character*
```

**style_note:**

![style_note](syntax/style_note.png)

```
style_note
         ::= 'os'
           | 'ns'
```

**calendar_system:**

![calendar_system](syntax/calendar_system.png)

```
calendar_system
         ::= '(' calendar_id ')'
```

**calendar_id:**

![calendar_id](syntax/calendar_id.png)

```
calendar_id
         ::= character_in_calendar_id+
```

referenced by:

* calendar_system

**character_in_calendar_id:**

![character_in_calendar_id](syntax/character_in_calendar_id.png)

```
character_in_calendar_id
         ::= [^)\n]
```

referenced by:

* calendar_id

**multi_date_choice:**

![multi_date_choice](syntax/multi_date_choice.png)

```
multi_date_choice
         ::= '[' date_choice ( '|' date_choice )* ']'
```

referenced by:

* month_component

**date_choice:**

![date_choice](syntax/date_choice.png)

```
date_choice
         ::= date_pair
           | day_range
```

referenced by:

* multi_date_choice

**date_pair:**

![date_pair](syntax/date_pair.png)

```
date_pair
         ::= month_number_literal '-' day_number_literal
```

referenced by:

* date_choice

**day_range:**

![day_range](syntax/day_range.png)

```
day_range
         ::= day_number_literal '..' [ '~] day_number_or_wildcard
```

referenced by:

* date_choice

**day_number_or_wildcard:**

![day_number_or_wildcard](syntax/day_number_or_wildcard.png)

```
day_number_or_wildcard
         ::= day_number_literal
           | '?'
```

referenced by:

* day_range

**year:**

![year](syntax/year.png)

```
year     ::= integer_number
           | '?'
           | temporal_integer_choice
```

referenced by:

* date_prefix
* day_of_year_expr
* half_year_expr
* ordinal_temporal_period_reference
* quarter_expr
* week_expr
* weighted_date_part

**century_number_literal:**

![century_number_literal](syntax/century_number_literal.png)

```
century_number_literal
         ::= digit+
```

referenced by:

* weighted_date_part

**integer_number:**

![integer_number](syntax/integer_number.png)

```
integer_number
         ::= [ '-'] digit+
```

referenced by:

* century_number
* integer_discrete
* integer_range
* year

**percentage:**

![percentage](syntax/percentage.png)

```
percentage
         ::= '100%'
           | digit digit '%'
```

referenced by:

* weighted_date_part

**number:**

![number](syntax/number.png)

```
number   ::= [ '-'] digit+ [ '.digt+]
```

referenced by:

* distribution_param
* geo_coordinates
* numeric_timeline_point
* uncertainty_asymmetric
* uncertainty_symmetric

**digit:**

![digit](syntax/digit.png)

```
digit    ::= '0'
           | '1'
           | '2'
           | '3'
           | '4'
           | '5'
           | '6'
           | '7'
           | '8'
           | '9'
```

referenced by:

* century_number_literal
* character_in_location_name
* character_in_timezone_id
* day_number_in_year
* day_number_literal
* decade_number
* fractional_seconds
* hour_literal
* integer_number
* label
* minute_literal
* number
* ordinal_number
* percentage
* second_literal
* week_expr

**letter:**

![letter](syntax/letter.png)

```
letter   ::= 'A' . . 'Z'
```

referenced by:

* character_in_location_name
* character_in_timezone_id
* label
* timezone_component

**character:**

![character](syntax/character.png)

```
character
         ::= [^\n]
```

referenced by:

* note_component

## 
![rr-2.5](syntax/rr-2.5.png) <sup>generated by [RR - Railroad Diagram Generator][RR]</sup>

[RR]: https://www.bottlecaps.de/rr/ui
