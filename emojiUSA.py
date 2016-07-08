## rebecca (marks) leopold, 2016
## http://www.twitter.com/emojiUSA
## http://oldobjectsnewideas.com/making-america-again/

## so much thx to Allison Parrish
## http://aparrish.neocities.org/twitter.html

## Need to install the following libraries
import emoji
import random
import twython

## Set up twitter developer
## http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/
api_key = " "
api_secret =  " " 
access_token =" "
token_secret = "  "

twitter = twython.Twython(api_key, api_secret, access_token, token_secret)

## I hard coded the emoji code by colors. 
## These are not all of them. But a good number.
## http://www.emoji-cheat-sheet.com/

red = [':rage:',':yum:',':broken_heart:', ':exclamation:', ':question:',
':japanese_goblin:',':japanese_ogre:', ':feet:', ':kiss:', ':love_letter:', 
':chicken:',':beetle:',':paw_prints:',':rose:', ':lips:', ':nail_care:',
':tongue:',':couplekiss:',':dancer:',':couple:',':runner:', ':couple_with_heart:',
':mushroom:',':volcano:',':no_bell:',':alarm_clock:', ':balloon:', 
':two_women_holding_hands:', ':family:',':heart_eyes:', ':blush:', ':kissing_heart:',
':stuck_out_tongue_winking_eye:',':stuck_out_tongue_closed_eyes:', ':flushed:',
':kissing_closed_eyes:',':yum:', ':anger:',':two_hearts:',':heartpulse:',
':heartbeat:',':heart:',':cupid:',':boom:',':collision:',':revolving_hearts:', 
':closed_book:', ':date:',':broken_heart:',':two_hearts:',':hibiscus:',':flags:',
':santa:',':phone:',':school_satchel:',':gift:',':name_badge:',':tada:',
':chart_with_upwards_trend:',':scissors:',':pushpin:',':baseball:',':sparkling_heart:',
':flower_playing_cards:',':dart:',':mahjong:',':art:',':high_heel:',':lipstick:'
,':sandal:',':ribbon:',':bookmark:',':memo:',':bicyclist:',':hearts:',
':snowboarder:',':diamonds:',':game_die:',':purse:',':wine_glass:',':pizza:',
':fries:',':poultry_leg:',':meat_on_bone:',':fried_shrimp:',':curry:'
,':spaghetti:',':bento:',':sushi:',':fish_cake:',':rice:',':ramen:',':birthday:',
':shaved_ice:',':cake:',':chocolate_bar:',':lollipop:',':apple:',':cherries:',
':strawberry:',':watermelon:',':peach:',':tomato:',':candy:',':house:',
':hospital:',':post_office:',':convenience_store:',':love_hotel:',':wedding:',
':hotel:',':department_store:',':city_sunrise:',':city_sunset:',':factory:',
':tokyo_tower:',':sunrise:',':european_castle:',':rainbow:',':bridge_at_night:',
':ferris_wheel:',':roller_coaster:',':boat:',':speedboat:',':ship:',':rowboat:',
':helicopter:',':rocket:',':steam_locomotive:',':car:',':red_car:',
':rotating_light:', ':police_car:',':oncoming_police_car:',':ambulance:',
':fire_engine:',':fuelpump:',':traffic_light:',':vertical_traffic_light:',
':barber:',':busstop:',':crossed_flags:',':hotsprings:',':izakaya_lantern:',
':circus_tent:',':round_pushpin:',':triangular_flag_on_post:',
':u5272:',':u5408:',':u6e80:',':womens:',
':cl:', ':sos:',':no_entry:',':no_mobile_phones:',':underage:',':o2:',
':no_pedestrians:',':no_entry_sign:',':do_not_litter:',':no_pedestrians:',
':non-potable_water:',':no_bicycles:',':a:',':b:',':ab:', ':heavy_exclamation_mark:',
':heavy_exclamation_mark:',':bangbang:',':interrobang:', ':x:',':o:',
':100:',':red_circle:', ':small_red_triangle:',':small_red_triangle:',
':small_red_triangle_down:',':white_flower:']

blue = [':sparkles:', ':star:', ':star2:', ':dizzy:', ':blue_heart:', ':zzz:',
 ':dash:', ':musical_note:',':bust_in_silhouette:',':busts_in_silhouette:',':pray:',
 ':cyclone:',':ocean:',':fish:',':whale:', ':purple_heart:',
':whale2:', ':dolphin:',':couple:', ':sweat_smile:',':sweat:', ':disappointed_relieved:',
':cold_sweat:',':fearful:',':joy:',':sob:',':cry:',':scream:',':sleepy:', ':innocent:',
':family:',':raised_hands:', ':two_men_holding_hands:',':globe_with_meridians:', 
':mailbox:',':shower:',':runner:', ':cop:',':angel:',
':e-mail:', ':mailbox_with_no_mail:',':blue_book:', ':globe_with_meridians:',
':earth_americas:',':earth_asia:', ':earth_africa:', ':milky_way:',
':alien:',':speech_balloon:',':thought_balloon:',':snowflake:',':cloud:',
':foggy:',':flags:',':computer:',':camera:',':cd:',':crystal_ball:',
':iphone:',':floppy_disk:',':fireworks:',':sparkler:',':mortar_board:',':dolls:',
':movie_camera:',':rice_scene:',':tv:',':calling:',':hammer:',':seat:',
':chart_with_downwards_trend:',':open_file_folder:',':books:',':newspaper:',
':gem:',':memo:',':headphones:',':shirt:',':tshirt:',':necktie:',
':running_shirt_with_sash:',':dress:',':bikini:',':kimono:',':jeans:',
':surfer:',':swimmer:',':ring:',':dart:',':book:',':fishing_pole_and_fish:',
':eyeglasses:',':baby_bottle:',':fork_and_knife:',':lollipop:',':eggplant:',
':house:',':hospital:',':post_office:',':office:',':bank:',':convenience_store:',
':hotel:',':department_store:',':european_castle:'+':japanese_castle:',
':mount_fuji:',':japan:',':stars:',':statue_of_liberty:',':rainbow:',
':carousel_horse:',':bridge_at_night:',':ferris_wheel:',':fountain:',
':roller_coaster:',':ship:',':rowboat:',':anchor:',':helicopter:',':airplane:',
':rocket:',':bike:',':oncoming_automobile:',':blue_car:',':police_car:',
':oncoming_police_car:',':train:',':bullettrain_side:',':trolleybus:',':barber:',
':busstop:',':performing_arts:',':arrow_forward:',
':arrow_left:',':arrow_right:',':abc:',':symbols:',':left_right_arrow:',
':arrow_up_down:',':arrows_counterclockwise:',':rewind:',':fast_forward:',
':information_source:',':repeat:',':twisted_rightwards_arrows:',':ok:',
':repeat_one:',':free:',':cool:',':up:', ':top:'+':new:',':cinema:',':sa:',
':restroom:',':mens:',':parking:',':wheelchair:',':passport_control:',
':diamond_shape_with_a_dot_inside:',':large_blue_diamond:',':large_blue_circle:',
':small_blue_diamond:']

## pick a random red emoji & a random blue emoji
star = random.choice(blue)
stripe = random.choice(red)

## make the emoji-code into emoji-icons
##print a number of times to form a flag shape
stars = ((emoji.emojize(star, use_aliases=True)) * 5)
shortStripes = (emoji.emojize(stripe, use_aliases=True)) * 7
longStripes = (emoji.emojize(stripe, use_aliases=True)) * 12

## tweet each pattern four times
twitter.update_status(status= ((stars + shortStripes + "\n") * 4) + ((longStripes + "\n") * 4))


# print ((stars + shortStripes + "\n") * 4) + ((longStripes + "\n") * 3)






