label cupboard:
    menu:
        "-Examine the cupboard-" if not cupboard_examined:
            $ cupboard_examined = True
            show screen chair_02 #Empty chair near the desk.
            hide screen genie
            $ tt_xpos=-20
            $ tt_ypos=100
            show screen genie_stands_f
            show screen desk
            with Dissolve(0.5)
            m "Hm....."
            m "A cupboard..."
            m "Maybe I should rummage through this one later..."
            show screen genie
            hide screen genie_stands_f
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
        
        "-Rummage through the cupboard-" if not searched and not day == 1:
            jump rummaging
        "{color=#858585}-Rummage through the cupboard-{/color}" if searched and not day == 1:
            call already_did #Message that says that you have searched the cupboard today already.
            jump cupboard
        
        "-Your possessions-" if not day == 1:
            label possessions:
            menu:
                "-Gift Items-" if cataloug_found:
                    label possessions_gift_items:
                    menu:
                        "-lollipop candy-([gift_item_inv[1]])" if gift_item_inv[1] >= 1:
                            call disp_gift_item(1)
                        "-Chocolate-([gift_item_inv[2]])" if gift_item_inv[2] >= 1:
                            call disp_gift_item(2)
                        "-Plush owl-([gift_item_inv[3]])" if gift_item_inv[3] >= 1:
                            call disp_gift_item(3)
                        "-Butterbeer-([gift_item_inv[4]])" if gift_item_inv[4] >= 1:
                            call disp_gift_item(4)
                        "-Educational magazines-([gift_item_inv[5]])" if gift_item_inv[5] >= 1:
                            call disp_gift_item(5)
                        "-Girly magazines-([gift_item_inv[6]])" if gift_item_inv[6] >= 1:
                            call disp_gift_item(6)
                        "-Adult magazines-([gift_item_inv[7]])" if gift_item_inv[7] >= 1:
                            call disp_gift_item(7)
                        "-Porn magazines-([gift_item_inv[8]])" if gift_item_inv[8] >= 1:
                            call disp_gift_item(8)
                        "-Viktor Krum Poster-([gift_item_inv[9]])" if gift_item_inv[9] >= 1:
                            call disp_gift_item(9)
                        "-Sexy lingerie-([gift_item_inv[10]])" if gift_item_inv[10] >= 1:
                            call disp_gift_item(10)
                        "-A pack of condoms-([gift_item_inv[11]])" if gift_item_inv[11] >= 1:
                            call disp_gift_item(11)
                        "-Vibrator-([gift_item_inv[12]])" if gift_item_inv[12] >= 1:
                            call disp_gift_item(12)
                        "-Jar of anal lubricant-([gift_item_inv[13]])" if gift_item_inv[13] >= 1:
                            call disp_gift_item(13)
                        "-Ball gag and cuffs-([gift_item_inv[14]])" if gift_item_inv[14] >= 1:
                            call disp_gift_item(14)
                        "-Anal plugs-([gift_item_inv[15]])" if gift_item_inv[15] >= 1:
                            call disp_gift_item(15)
                        "-Thestral Strap-on-([gift_item_inv[16]])" if gift_item_inv[16] >= 1:
                            call disp_gift_item(16)
                        "-Lady Speed Stick-2000-([gift_item_inv[17]])" if gift_item_inv[17] >= 1:
                            call disp_gift_item(17)
                        "-Sex doll \"Joanne\"-([gift_item_inv[18]])" if gift_item_inv[18] >= 1:
                            call disp_gift_item(18)
                        "-Tentacle Scroll-" if tentacle_owned:
                            ">Should I use this scroll..."
                            menu:
                                "\"(Yes, let's do it!)\"":
                                    jump tentacle_scene_intro
                                "\"(Not right now.)\"":
                                    jump possessions
                        "-Tentacle Scroll-" if tent_scroll and not tentacle_owned:
                            m "It's missing the key ingredient."
                            jump possessions
                        "-Never mind-":
                            jump possessions
                
                "-Clothing-"if False:
                    label possessions_clothing:
                    menu:
                        "-Never mind-":
                            jump possessions
                
                "-Potion Items-" if False:
                    label possessions_potions:
                    menu:
                        "-Crafting Items-" if False:
                            label possessions_potion_items:
                            menu:
                                "-Never mind-":
                                    jump possessions_potions
                        "-Potions-":
                            label possessions_complete_potions:
                            menu:
                                "-Cum Addiction Potion-" if "Cum Addiction Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Ass Expansion Potion-" if "Ass Expansion Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Breast Expansion Potion-" if "Breast Expansion Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Cat Transformation Potion-" if "Cat Transformation Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Luna Transformation Potion-" if "Luna Transformation Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Lamia Transformation Potion-" if "Lamia Transformation Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Transparency Potion-" if "Transparency Potion" in p_inv:
                                    jump possessions_complete_potions
                                "-Never mind-":
                                    jump possessions_potions
                        "-Never mind-":
                            jump possessions
                    
                "-The Ball Dress-" if "ball_dress" in gifts12 and not gave_the_dress:
                    $ the_gift = "01_hp/18_store/01.png" # DRESS.
                    show screen gift
                    with d3
                    m "A fancy night dress I bought..."
                    m "I hope it's the right size."
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-\"S.P.E.W.\" Badge-" if badge_01 == 1:
                    $ the_gift = "01_hp/18_store/29.png" # S.P.E.W. BADGE
                    show screen gift
                    with d3
                    m "A \"S.P.E.W.\" Badge..."
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-Fishnet stockings-" if nets == 1:
                    $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
                    show screen gift
                    with d3
                    call nets_text
                    hide screen gift
                    with d3
                    jump possessions
                    
                "-School miniskirt-" if have_miniskirt:
                    $ the_gift = "01_hp/18_store/07.png" # MINISKIRT.
                    show screen gift
                    with d3
                    m "A school miniskirt... Improves grades drastically."
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Dumbledor's Wine-([wine])" if wine >= 1:
                    $ the_gift = "01_hp/18_store/27.png" # WINE.
                    show screen gift
                    with d3
                    ">A bottle of wine from professor dumbledore's personal stash..." 
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Unknown potion-([potions])" if  potions >= 1:
                    $ the_gift = "01_hp/18_store/32.png" # HEALING POTION.
                    show screen gift
                    with d3
                    ">A potion of some sort..." 
                    hide screen gift
                    with d3
                    jump possessions
                
                "-Sacred scrolls volume I-" if cataloug_found:
                    label sc_col_men:
                    menu:
                        "-S.01: [scroll_name_[1]]-" if sscroll_[1] or persistent.ss_01:
                            call disp_sacred_scrolls(1)
                            jump sc_col_men
                            
                        "-S.02: [scroll_name_[2]]-" if sscroll_[2] or persistent.ss_02:
                            call disp_sacred_scrolls(2)
                            jump sc_col_men
                            
                        "-S.03: [scroll_name_[3]]-" if sscroll_[3] or persistent.ss_03:
                            call disp_sacred_scrolls(3)
                            jump sc_col_men
                            
                        "-S.04: [scroll_name_[4]]-" if sscroll_[4] or persistent.ss_04:
                            call disp_sacred_scrolls(4)
                            jump sc_col_men
                            
                        "-S.05: [scroll_name_[5]]-" if sscroll_[5] or persistent.ss_05:
                            call disp_sacred_scrolls(5)
                            jump sc_col_men
                            
                        "-S.06: [scroll_name_[6]]-" if sscroll_[6] or persistent.ss_06:
                            call disp_sacred_scrolls(6)
                            jump sc_col_men
                            
                        "-S.07: [scroll_name_[7]]-" if sscroll_[7] or persistent.ss_07:
                            call disp_sacred_scrolls(7)
                            jump sc_col_men
                            
                        "-S.08: [scroll_name_[8]]-" if sscroll_[8] or persistent.ss_08:
                            call disp_sacred_scrolls(8)
                            jump sc_col_men
                            
                        "-S.09: [scroll_name_[9]]-" if sscroll_[9] or persistent.ss_09:
                            call disp_sacred_scrolls(9)
                            jump sc_col_men
                            
                        "-S.10: [scroll_name_[10]]-" if sscroll_[10] or persistent.ss_10:
                            call disp_sacred_scrolls(10)
                            jump sc_col_men
                        
                        "-S.11: [scroll_name_[11]]-" if sscroll_[11] or persistent.ss_11:
                            call disp_sacred_scrolls(11)
                            jump sc_col_men
                        
                        "-S.12: [scroll_name_[12]]-" if sscroll_[12] or persistent.ss_12:
                            call disp_sacred_scrolls(12)
                            jump sc_col_men
                        
                        "-S.13: [scroll_name_[13]]-" if sscroll_[13] or persistent.ss_13:
                            call disp_sacred_scrolls(13)
                            jump sc_col_men
                        
                        "-S.14: [scroll_name_[14]]-" if sscroll_[14] or persistent.ss_14:
                            call disp_sacred_scrolls(14)
                            jump sc_col_men
                        
                        "-S.15: [scroll_name_[15]]-" if sscroll_[15] or persistent.ss_15:
                            call disp_sacred_scrolls(15)
                            jump sc_col_men

                        "-Never mind-":
                            jump possessions
                
                "-Sacred scrolls volume II-" if cataloug_found:
                    label sc_col_men2:
                    menu:
                        "-S.16: [scroll_name_[16]]-" if sscroll_[16] or persistent.ss_16:
                            call disp_sacred_scrolls(16)
                            jump sc_col_men2
                            
                        "-S.17: [scroll_name_[17]]-" if sscroll_[17] or persistent.ss_17:
                            call disp_sacred_scrolls(17)
                            jump sc_col_men2
                            
                        "-S.18: [scroll_name_[18]]-" if sscroll_[18] or persistent.ss_18:
                            call disp_sacred_scrolls(18)
                            jump sc_col_men2
                            
                        "-S.19: [scroll_name_[19]]-" if sscroll_[19] or persistent.ss_19:
                            call disp_sacred_scrolls(19)
                            jump sc_col_men2
                            
                        "-S.20: [scroll_name_[20]]-" if sscroll_[20] or persistent.ss_20:
                            call disp_sacred_scrolls(20)
                            jump sc_col_men2
                            
                        "-S.21: [scroll_name_[21]]-" if sscroll_[21] or persistent.ss_21:
                            call disp_sacred_scrolls(21)
                            jump sc_col_men2
                            
                        "-S.22: [scroll_name_[22]]-" if sscroll_[22] or persistent.ss_22:
                            call disp_sacred_scrolls(22)
                            jump sc_col_men2
                            
                        "-S.23: [scroll_name_[23]]-" if sscroll_[23] or persistent.ss_23:
                            call disp_sacred_scrolls(23)
                            jump sc_col_men2
                            
                        "-S.24: [scroll_name_[24]]-" if sscroll_[24] or persistent.ss_24:
                            call disp_sacred_scrolls(24)
                            jump sc_col_men2
                            
                        "-S.25: [scroll_name_[25]]-" if sscroll_[25] or persistent.ss_25:
                            call disp_sacred_scrolls(25)
                            jump sc_col_men2
                        
                        "-S.26: [scroll_name_[26]]-" if sscroll_[26] or persistent.ss_26:
                            call disp_sacred_scrolls(26)
                            jump sc_col_men2
                        
                        "-S.27: [scroll_name_[27]]-" if sscroll_[27] or persistent.ss_27:
                            call disp_sacred_scrolls(27)
                            jump sc_col_men2
                        
                        "-S.28: [scroll_name_[28]]-" if sscroll_[28] or persistent.ss_28:
                            call disp_sacred_scrolls(28)
                            jump sc_col_men2
                        
                        "-S.29: [scroll_name_[29]]-" if sscroll_[29] or persistent.ss_29:
                            call disp_sacred_scrolls(29)
                            jump sc_col_men2
                        
                        "-S.30: [scroll_name_[30]]-" if sscroll_[30] or persistent.ss_30:
                            call disp_sacred_scrolls(30)
                            jump sc_col_men2

                        "-Never mind-":
                            jump possessions
                
                "-Never mind-":
                    jump cupboard
        
        "-Potion crafting-" if shop_found:
            jump potion_menu
        
        "-Change Save Name-":
            jump custom_save
        
        "-Cheat-":
            jump cheats_ht
        
        "-Never mind-":
            jump day_main_menu

label custom_save:
    $ temp_name = renpy.input("(Please enter the save name.)")
    $ temp_name = temp_name.strip()
    if temp_name == "":
        $ temp_name = "Day - "+str(day)+"\nWhoring - "+str(whoring)
    $ save_name = temp_name
    "Done."
    jump cupboard
label rummaging:  
    
    $ searched = True #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
    
    $ rum_times += 1 # Counts how many times have you rummaged the cupboard. +1 every time you do that. Needed to make to grand 2 potions before the fight.
    
    hide screen cupboard
    hide screen genie
    show screen rum_screen
    with Dissolve(0.3)
    show screen bld1
    with d3
    ">You rummage through the cupboard for a while..." 
    
    if day <= 4:
        if rum_times == 2 or rum_times == 3:
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ potions += 1
            $ the_gift = "01_hp/18_store/32.png"
            show screen gift
            with d3
            ">You found some sort of potion..." 
            hide screen gift
            with d3
            show screen cupboard
            show screen genie
            hide screen rum_screen
            
            hide screen bld1
            with d3
            
            if daytime:
                jump night_start
            else: 
                jump day_start
    
    if rum_times >= 7 and not cataloug_found:
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ cataloug_found = True # Turns TRUE after you found the Dahr's oddities catalog in the cupboard.
        $ the_gift = "01_hp/18_store/31.png" # DAHR's oddities catalog. 
        show screen gift
        with d3
        ">You found a map of the school grounds...\n>You can now leave the office."
        hide screen gift
        with d3
        show screen cupboard
        show screen genie
        hide screen rum_screen
        
        hide screen bld1
        with d3
        
        if daytime:
            jump night_start
        else: 
            jump day_start
        
    
    if i_of_iv == 4: # Found something.
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            if one_of_tw == 20:# SEX DOLL.
                call rum_block(18)
            elif one_of_tw == 1 or one_of_tw == 2:# CANDY.
                call rum_block(1)
            elif one_of_tw >= 3 and one_of_tw <= 9  or one_of_tw == 18: # GOLD.
                call rum_block("gold1")
            elif one_of_tw >= 10 and one_of_tw <= 16: # WINE.
                call rum_block("wine")
            elif one_of_tw == 17: # CHOCOLATE.
                call rum_block(2)
            elif one_of_tw == 19: # LINGERIE.
                call rum_block(10)
        
        
        ### EVENT LEVEL 02 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 6 and whoring <= 11: # Lv 3-4. 
            if one_of_tw == 20:# SEX DOLL.
                call rum_block(18)
            elif one_of_tw == 1 or one_of_tw ==2:# CANDY.
                call rum_block(1)
            elif one_of_tw >= 3 and one_of_tw <= 10 or one_of_tw == 18:# GOLD.
                call rum_block("gold2")
            elif one_of_tw >= 11 and one_of_tw <= 15:# WINE
                call rum_block("wine")
            elif one_of_tw == 16:# LINGERIE
                call rum_block(10)
            elif one_of_tw == 17:# CHOCOLATE.
                call rum_block(2)
            elif one_of_tw == 19:# KRUM POSTER.
                call rum_block(9)
        
        
        ### EVENT LEVEL 03 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            if one_of_tw == 20:# SEX DOLL.
                call rum_block(18)
            elif one_of_tw >= 1 and one_of_tw <= 4:
                call rum_block(3)
            elif one_of_tw == 5 or one_of_tw == 6:
                call rum_block(1)
            elif one_of_tw >= 7 and one_of_tw <= 14:
                call rum_block("gold3")
            elif one_of_tw >= 15 and one_of_tw <= 18:
                call rum_block("wine")
            elif one_of_tw == 19:
                call rum_block(9)
        
        
        ### EVENT LEVEL 04 ###  ### ###  ### ###  ###  ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ### ###  ###
        if whoring >= 18: # Lv 7+  
            if one_of_tw == 20:
                call rum_block(18)
            elif one_of_tw >= 1 and one_of_tw <= 4:
                call rum_block(3)
            elif one_of_tw >= 5 and one_of_tw <= 8:
                call rum_block(2)
            elif one_of_tw >= 9 and one_of_tw <= 16:
                call rum_block("gold4")
            elif one_of_tw == 17:
                call rum_block(17)
            elif one_of_tw == 18:
                call rum_block(9)
            elif one_of_tw == 19:
                call rum_block(10)
            
            
    else: #Didn't find anything.
        ">...You find nothing of value." 
    

    
    show screen cupboard
    show screen genie
    hide screen rum_screen
    
    hide screen bld1
    with d3
    
    if daytime:
        jump day_main_menu
    else: 
        jump night_main_menu
        
label disp_gift_item(item):
    $ the_gift = "01_hp/18_store/gifts/"+str(item)+".png" # CANDY.
    show screen gift
    with d3
    $ text = gift_description[item]
    ">[text]"
    hide screen gift
    with d3
    jump possessions_gift_items
    
label disp_sacred_scrolls(scroll):
    $ the_gift = "01_hp/19_extras/"+str(scroll)+".png" # SACRED SCROLL
    show screen gift
    show screen ctc
    with d3
    pause
    hide screen gift
    hide screen ctc
    with d3
    return
        
label rum_block(item):
    if isinstance( item, int ):
        $ renpy.play('sounds/win2.mp3')   #Not loud.
        $ gift_item_inv[item] += 1
        $ the_gift = "01_hp/18_store/gifts/"+str(item)+".png" # LINGERIE
        show screen gift
        with d3
        $ tmp_str = "You found "+store_gift_items[item]+"..."
        ">[tmp_str]"
        $ tmp_str = gift_description[item]
        ">[tmp_str]"
        hide screen gift
        with d3
    else:
        if "wine" in item:
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ wine += 1
            $ the_gift = "01_hp/18_store/27.png" # WINE
            show screen gift
            with d3
            ">You found a bottle of wine from professor dumbledore's personal stash..." 
            hide screen gift
            with d3
        if "gold" in item:
            if item == "gold1":
                $ tmp_gold = gold1
            if item == "gold2":
                $ tmp_gold = gold2
            if item == "gold3":
                $ tmp_gold = gold3
            if item == "gold4":
                $ tmp_gold = gold4
            $ renpy.play('sounds/win2.mp3')   #Not loud.
            $ the_gift = "01_hp/18_store/28.png" # GOLD.
            show screen gift
            with d3
            ">You found [tmp_gold] gold..." 
            $ gold += tmp_gold
            hide screen gift
            with d3
    return
        
        
        
######################
label already_did:
    show screen bld1
    with d3
    m "I already did that today..."
    hide screen bld1
    with d3
    return