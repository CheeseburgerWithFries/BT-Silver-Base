label __init_variables:
    
    $ h_whoring = 0
    $ h_reputation = 21
    
    if not hasattr(renpy.store,'hermione_xpos'): #important!
        $ hermione_xpos = 370
    if not hasattr(renpy.store,'hermione_ypos'): #important!
        $ hermione_ypos = 0
    if not hasattr(renpy.store,'hermione_head_xpos'): #important!
        $ hermione_head_xpos = 390
    if not hasattr(renpy.store,'hermione_head_ypos'): #important!
        $ hermione_head_ypos = 235
    
    $ hermione_body = "01_hp/13_characters/hermione/body/face/body_01.png"
    $ hermione_tears = "01_hp/13_characters/hermione/body/face/tears/00_blank.png"
    $ hermione_base = "01_hp/13_characters/hermione/body/base/hermione_base.png"
    $ hermione_legs  = "01_hp/13_characters/hermione/body/legs/legs_1.png"
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_1.png"
    $ hermione_left_arm = "01_hp/13_characters/hermione/body/arms/left/left_1.png"
    $ hermione_right_arm = "01_hp/13_characters/hermione/body/arms/right/right_1.png"
    $ hermione_emote = "01_hp/13_characters/emote/00_blank.png"
    
    $ h_body = "body_01"
    $ h_tears = "00_blank"
    $ h_bra = "base_bra_white_1"
    $ h_panties = "base_panties_1"
    $ h_skirt = 1
    $ h_top = 1
    
    if not hasattr(renpy.store,'hermione_hair_a'): #important!
        $ hermione_hair_a = "01_hp/13_characters/hermione/body/head/A_1.png"
    if not hasattr(renpy.store,'hermione_hair_b'): #important!
        $ hermione_hair_b = "01_hp/13_characters/hermione/body/head/A_1_2.png"
    if not hasattr(renpy.store,'h_hair_style'): #important!
        $ h_hair_style = "A"
    if not hasattr(renpy.store,'h_hair_color'): #important!
        $ h_hair_color = 1
    
    
    $ hermione_zorder = 5
    
    $ hermione_badge = "01_hp/13_characters/hermione/clothes/badges/spew_badge.png"
    
    if not hasattr(renpy.store,'hermione_skirt'): #important!
        $ hermione_skirt = "01_hp/13_characters/hermione/clothes/uniform/skirt_1.png"
    if not hasattr(renpy.store,'hermione_top'): #important!
        $ hermione_top = "01_hp/13_characters/hermione/clothes/uniform/top_1.png"
    
    $ hermione_bra = "01_hp/13_characters/hermione/clothes/underwear/base_bra_white_1.png"
    $ hermione_panties = "01_hp/13_characters/hermione/clothes/underwear/base_panties_1.png"
    $ hermione_stockings = "01_hp/13_characters/hermione/clothes/stockings/00_blank.png"
    
    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe.png"
    
    
    
    
    $ hermione_wear_robe = False
    
    $ hermione_wear_bra = True
    $ hermione_wear_panties = True
    $ hermione_wear_skirt = True
    $ hermione_wear_top = True
    
    $ hermione_badges = False
    
    $ hermione_perm_expand = False
    
    $ h_display_tears = False
    $ h_request_wear_panties = False
    
    
    $ h_badge = "spew_badge"
    $ h_stocking = "00_blank"
    $ h_breasts = 1
    $ h_bra_nip_fix = ["cup_bra","silk_bra","latex_bra"]
    
    
    ## Chibi Vars
    $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_a_01.png"
    $ hermione_chibi_blink = "ch_hem blink_a"
    $ hermione_chibi_blink_f = "ch_hem blink_a_flip"
    $ hermione_chibi_walk = "ch_hem walk_a"
    $ hermione_chibi_walk_f = "ch_hem walk_a_flip"
    $ hermione_chibi_zorder = 3
    
    ## Action Vars
    if not hasattr(renpy.store,'hermione_action'): #important!
        $ hermione_action = False
    
    $ hermiome_action_bra = hermione_bra
    $ hermiome_action_panties = hermione_panties
    $ hermiome_action_top = hermione_top
    $ hermiome_action_skirt = hermione_skirt
    
    $ hermiome_action_a = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    $ hermiome_action_b = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    
    $ h_action_a = "00_blank.png"
    $ h_action_b = "00_blank.png"
    
    $ h_action_show_bra = True
    $ h_action_show_panties = True
    $ h_action_show_top = True
    $ h_action_show_skirt = True
    
    ## Emote Vars
    $ hermione_emote_anger = False
    $ hermione_emote_exclam = False
    $ hermione_emote_hearts = False
    $ hermione_emote_question = False
    $ hermione_emote_sweat = False
    $ hermione_emote_suprize = False
    $ hermione_anger = ["body_51","body_76","body_86","body_110","body_218","body_351","body_346","body_345","body_343","body_317","body_309","head_exp/24"]
    $ hermione_exclam = ["head_exp/30"]
    $ hermione_hearts = []
    $ hermione_question = []
    $ hermione_sweat = ["body_24","body_34","body_57","body_108","body_208","body_340","head_exp/9"]
    $ hermione_suprize = ["body_80","body_80b","body_335"]
    
    
    
    $ u_h_animation = ""
    $ u_h_animation_paused = ""
    $ u_h_ani_xpos = 0
    $ u_h_ani_ypos = 0
    
    
    
    ## Custom Clothes/Outfits Vars
    if not hasattr(renpy.store,'custom_outfit'): #important!
        $ custom_outfit = 0
    if not hasattr(renpy.store,'hermione_custom_outfit'): #important!
        $ hermione_custom_outfit = False
    if not hasattr(renpy.store,'hermione_custom_a'): #important!
        $ hermione_custom_a = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    if not hasattr(renpy.store,'hermione_custom_b'): #important!
        $ hermione_custom_b = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    if not hasattr(renpy.store,'hermione_custom_c'): #important!
        $ hermione_custom_c = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    if not hasattr(renpy.store,'hermione_custom_d'): #important!
        $ hermione_custom_d = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    if not hasattr(renpy.store,'hermione_custom_e'): #important!
        $ hermione_custom_e = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    if not hasattr(renpy.store,'hermione_custom_action_a'): #important!
        $ hermione_custom_action_a = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    
    $ outfit_set_size = 20
    
    #if not hasattr(renpy.store,'hermione_custom_hair_list'): #important!
    $ hermione_custom_hair_list = [""] * outfit_set_size
    $ hermione_custom_hair_list[7] = ("power_hair")
    $ hermione_custom_hair_list[9] = ("harley_hair")
    
    $ hermione_custom_breast_list = ["breasts_1"] * outfit_set_size
    $ hermione_custom_breast_list[11] = "breasts_2"
    
    #if not hasattr(renpy.store,'hermione_custom_outfit_list'): #important!
    $ hermione_custom_outfit_list = [[0 for i in xrange(5)] for i in xrange(outfit_set_size)]
    
    $ hermione_custom_outfit_list [1][0] = "maid_stockings.png" 
    $ hermione_custom_outfit_list [1][1] = "maid_skirt.png"
    $ hermione_custom_outfit_list [1][2] = "maid_top.png"
    $ hermione_custom_outfit_list [1][3] = "maid_gloves.png"
    $ hermione_custom_outfit_list [1][4] = "maid_hat.png"
    
    $ hermione_custom_outfit_list [2][0] = "cheer_stockings.png" 
    $ hermione_custom_outfit_list [2][1] = "cheer_pants.png"
    $ hermione_custom_outfit_list [2][2] = "cheer_top.png"
    $ hermione_custom_outfit_list [2][3] = ""
    $ hermione_custom_outfit_list [2][4] = ""
    
    $ hermione_custom_outfit_list [3][0] = "s_cheer_stockings.png" 
    $ hermione_custom_outfit_list [3][1] = "s_cheer_pants.png"
    $ hermione_custom_outfit_list [3][2] = "s_cheer_top.png"
    $ hermione_custom_outfit_list [3][3] = ""
    $ hermione_custom_outfit_list [3][4] = ""
    
    $ hermione_custom_outfit_list [4][0] = "heart_legs.png" 
    $ hermione_custom_outfit_list [4][1] = "heart_top.png"
    $ hermione_custom_outfit_list [4][2] = "heart_collar.png"
    $ hermione_custom_outfit_list [4][3] = ""
    $ hermione_custom_outfit_list [4][4] = ""
    
    $ hermione_custom_outfit_list [5][0] = "" 
    $ hermione_custom_outfit_list [5][1] = ""
    $ hermione_custom_outfit_list [5][2] = ""
    $ hermione_custom_outfit_list [5][3] = ""
    $ hermione_custom_outfit_list [5][4] = ""
    
    $ hermione_custom_outfit_list [6][0] = "" 
    $ hermione_custom_outfit_list [6][1] = ""
    $ hermione_custom_outfit_list [6][2] = ""
    $ hermione_custom_outfit_list [6][3] = ""
    $ hermione_custom_outfit_list [6][4] = ""
    
    $ hermione_custom_outfit_list [7][0] = "power_costume.png" 
    $ hermione_custom_outfit_list [7][1] = ""
    $ hermione_custom_outfit_list [7][2] = ""
    $ hermione_custom_outfit_list [7][3] = ""
    $ hermione_custom_outfit_list [7][4] = ""
    
    $ hermione_custom_outfit_list [8][0] = "marvel_pants.png" 
    $ hermione_custom_outfit_list [8][1] = "marvel_top.png"
    $ hermione_custom_outfit_list [8][2] = "marvel_sash.png"
    $ hermione_custom_outfit_list [8][3] = "marvel_gloves.png"
    $ hermione_custom_outfit_list [8][4] = ""
    
    $ hermione_custom_outfit_list [9][0] = "harley_pants.png" 
    $ hermione_custom_outfit_list [9][1] = "harley_top.png"
    $ hermione_custom_outfit_list [9][2] = "harley_gloves.png"
    $ hermione_custom_outfit_list [9][3] = "harley_collar.png"
    $ hermione_custom_outfit_list [9][4] = ""
    
    $ hermione_custom_outfit_list [10][0] = "ball_dress_skirt.png" 
    $ hermione_custom_outfit_list [10][1] = "ball_dress_top.png"
    $ hermione_custom_outfit_list [10][2] = ""
    $ hermione_custom_outfit_list [10][3] = ""
    $ hermione_custom_outfit_list [10][4] = ""
    
    $ hermione_custom_outfit_list [11][0] = "christmas_pants.png" 
    $ hermione_custom_outfit_list [11][1] = "christmas_top.png"
    $ hermione_custom_outfit_list [11][2] = "christmas_gloves.png"
    $ hermione_custom_outfit_list [11][3] = "christmas_collar.png"
    $ hermione_custom_outfit_list [11][4] = "christmas_antlers.png"
    
    $ hermione_custom_outfit_list [12][0] = "lara_pants.png" 
    $ hermione_custom_outfit_list [12][1] = "lara_top.png"
    $ hermione_custom_outfit_list [12][2] = "lara_gloves.png"
    $ hermione_custom_outfit_list [12][3] = ""
    $ hermione_custom_outfit_list [12][4] = ""
    
    #if not hasattr(renpy.store,'h_current_sets'): #important!
    $ h_current_sets = 12
    
    
    
    return