# -*- coding: utf-8 -*-
#==============================================================================#
#                                                                              #
#    Offline KI                                                                #
#    See the file AUTHORS for more info about the contributors.                #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                      #
#                                                                              #
#    You may re-use the code in this file within the context of Uru.           #
#                                                                              #
#==============================================================================#
from Plasma import *

# begin of CameraTours
CameraTours = {
    'city': {
        'grandtour':
            ([(-109.131897,-229.774216,309.235596),(-107.105347,-227.562180,308.235596)],
            [(-221.661270,-224.432144,221.217484),(-219.023621,-223.002869,220.217484)],
            [(14.313814,-153.595032,279.372498),(11.984230,-151.704788,277.372498)],
            [(6.283119,-143.828705,279.371948),(8.971365,-142.497040,277.371948)],
            [(-49.742638,-72.413857,279.339447),(-46.934875,-71.357216,278.339447)],
            [(175.322006,24.138821,297.370361),(178.010254,25.470484,297.370361)],
            [(278.883453,90.767746,319.370361),(279.324463,87.800339,317.370361)],
            [(346.250305,-11.088562,305.355225),(345.735901,-8.132994,305.355225)],
            [(383.532837,-236.940948,305.355225),(383.316071,-233.948792,304.355225)],
            [(459.720123,-72.995872,302.594604),(456.722656,-73.118805,300.594604)],
            [(465.174774,-79.449013,315.874054),(467.458252,-81.394714,314.874054)],
            [(524.161316,-268.848877,363.600677),(527.097900,-269.462311,362.600677)],
            [(802.808228,-335.277283,319.351379),(801.800171,-338.102844,318.351379)],
            [(623.013306,-532.648376,297.351379),(625.890991,-531.800537,296.351379)],
            [(722.486755,-506.213074,312.647797),(724.554688,-508.386475,311.647797)],
            [(858.373779,-665.137512,254.647797),(861.372681,-665.218750,253.647797)],
            [(858.373779,-665.137512,254.647797),(859.097717,-668.048828,253.647797)],
            [(898.269958,-727.509094,235.647797),(896.870483,-724.855530,234.647797)],
            [(874.543274,-699.195862,221.647797),(876.920410,-697.365784,221.647797)],
            [(895.282104,-877.131104,308.647797),(895.675476,-874.156982,307.647797)],
            [(513.348267,-376.688202,338.647797),(512.267639,-373.889587,337.647797)],
            [(528.491455,-312.448944,312.647797),(526.011536,-314.137177,312.647797)],
            [(399.147736,-466.417725,301.719269),(399.986664,-469.298035,300.719269)],
            [(364.118713,-561.752747,250.377289),(363.051575,-558.948975,249.377289)],
            [(327.366699,-496.734375,256.377289),(324.576355,-497.836151,255.377289)],
            [(260.280548,-538.347229,247.294739),(257.704468,-536.809814,245.294739)],
            [(217.959778,-509.522614,219.146515),(219.171448,-506.778198,218.146515)],
            [(242.888321,-465.049896,216.204346),(245.501114,-463.575653,215.204346)],
            [(302.573212,-419.933624,195.361572),(299.938263,-418.499359,194.361572)],
            [(206.654007,-360.090973,197.614700),(204.409882,-358.100006,196.614700)],
            [(112.689087,-273.509460,201.614700),(115.014046,-275.405396,200.614700)],
            [(168.461594,-408.747589,201.283920),(168.303726,-405.751740,199.283920)],
            [(156.804916,-388.042664,195.283920),(159.319946,-389.678101,194.283920)],
            [(170.644287,-386.072205,195.283920),(168.283600,-387.923462,194.283920)],
            [(170.288971,-413.060272,205.283920),(170.271683,-416.060211,203.283920)],
            [(145.344269,-516.673523,198.283920),(146.642014,-513.968750,197.283920)],
            [(183.562088,-520.761230,198.283920),(182.525940,-517.945862,197.283920)],
            [(58.145775,-221.148712,239.283920),(57.689632,-218.183594,238.283920)],
            [(-1.870446,-123.232231,249.283920),(-1.837312,-126.232048,247.283920)],
            [(-0.578197,-240.225098,181.283920),(-0.545062,-243.224915,179.283920)],
            [(27.435228,-354.042084,157.283920),(26.685354,-351.137329,156.283920)],
            [(-47.959751,-341.798889,179.283920),(-46.661987,-339.094116,177.283920)],
            [(-25.103426,-290.204041,150.863159),(-28.103279,-290.233673,149.863159)],
            [(-137.343826,-291.550720,140.863159),(-134.347794,-291.396362,139.863159)],
            [(-128.232407,-302.385040,139.863159),(-127.875298,-299.406372,138.863159)],
            [(-146.319611,-252.270050,145.863159),(-143.352646,-252.713989,143.863159)],
            [(-157.853683,-237.981201,142.863159),(-155.132645,-236.717896,141.863159)],
            [(-90.821037,-227.847794,141.863159),(-93.757034,-227.231415,140.863159)],
            [(1.528685,-313.646149,151.571777),(1.563458,-316.645935,149.571777)],
            [(-41.424202,-368.281647,126.571777),(-39.701691,-370.737854,124.571777)],
            [(78.568939,-548.784180,115.571777),(77.768745,-545.892883,114.271774)],
            [(94.767601,-490.244934,96.571777),(91.767601,-490.242523,95.071777)],
            [(-15.290363,-601.484863,56.571777),(-17.615551,-599.589233,55.571777)],
            [(-15.290363,-601.484863,56.571777),(-13.327624,-599.216003,55.571777)],
            [(97.955887,-555.311829,19.571777),(100.868187,-556.031921,18.571777)],
            [(-325.278381,-628.192017,46.571777),(-322.732819,-626.604553,45.571777)],
            [(-415.038513,-347.196472,46.571777),(-412.327332,-348.480774,45.571777)],
            [(-5.893919,-818.913147,197.571777),(-5.854366,-815.913391,196.571777)],
            [(-98.605942,-231.933304,320.571777),(-96.879524,-229.479843,319.571777)]),
    },
    'BaronCityOffice': {
        'sharper1':
            ([(5.454856,16.997099,5.007216),(8.453029,16.892405,5.007216)],
            [(-7.072324,23.980524,5.003830),(-9.489861,25.756901,5.003830)],
            [(7.809386,8.559968,5.011423),(10.402374,7.051190,6.011423)],
            [(-7.571403,8.988198,5.010916),(-10.264578,7.666530,6.010916)],
            [(4.486110,-23.625387,5.003055),(6.819992,-25.510326,6.003055)],
            [(0.532821,-24.903345,5.006388),(0.471590,-27.902719,6.006388)],
            [(-4.833063,-23.281664,5.013317),(-7.257656,-25.048397,6.013317)],
            [(0.585273,22.347752,5.011432),(0.730903,19.351288,2.011432)],
            [(0.991356,5.606924,5.005991),(0.960960,2.607078,5.005991)],
            [(5.924450,-16.032482,5.002796),(8.910572,-15.744255,5.002796)],
            [(1.897020,-3.136791,5.011059),(1.590805,-0.152460,5.011059)],
            [(-0.032804,-30.233978,5.000196),(0.071206,-27.235783,5.000196)],
            [(24.680086,-12.055087,3.849993),(21.743938,-12.670746,4.849994)],
            [(42.914383,17.856741,3.850378),(39.915211,17.786243,3.850378)],
            [(5.454856,16.997099,5.007216),(8.453029,16.892405,5.007216)]),
    },

    'Neighborhood': {
        # Hood Tour by LCC
        'hoodtour1':
            ([(306.706085,-906.701416,44.699604),(305.425903,-903.988281,42.699604)],
            [(7.251385,-773.143616,33.101707),(4.301781,-772.596069,29.101707)],
            [(46.010803,-791.237366,88.156891),(43.108009,-791.994873,88.156891)],
            [(33.762508,-835.009216,13.086222),(35.678383,-832.700684,13.086222)],
            [(166.952240,-765.206970,36.915581),(165.019165,-762.912781,36.915581)],
            [(304.270569,-722.831604,24.127951),(305.381409,-720.044861,24.127951)],
            [(186.781204,-865.765747,-13.312992),(183.965622,-866.801392,-13.312992)],
            [(186.121277,-868.188049,-13.287674),(188.220093,-870.331665,-13.287674)],
            [(281.354431,-856.806030,10.707239),(282.677521,-859.498535,10.707239)],
            [(133.035522,-756.561523,14.430536),(130.388016,-757.972473,14.430536)],
            [(234.530426,-765.009338,14.819983),(231.569077,-764.529358,14.819983)],
            [(286.895538,-815.240601,2.597646),(289.832916,-814.630798,3.597646)],
            [(252.610703,-848.388855,7.697535),(253.804962,-851.140869,7.697535)],
            [(293.306519,-830.772095,7.599095),(294.581879,-833.487488,7.599095)],
            [(295.826416,-799.889709,97.599495),(293.143341,-801.231750,52.599495)],
            [(240.750336,-819.266052,7.600081),(238.039124,-820.550293,7.600081)],
            [(238.706573,-848.824097,2.669274),(240.524719,-846.437805,2.669274)],
            [(233.998932,-814.774475,7.599081),(231.096405,-814.015991,7.599081)],
            [(306.706085,-906.701416,44.699604),(305.425903,-903.988281,42.699604)]),
    },

    'Teledahn': {
        'cavetour':
            ([(-89.479591,-172.350143,-36.018723),(-88.527679,-175.195114,-42.018723)],
            [(-87.958038,-176.495392,-72.139931),(-89.038116,-179.294220,-71.139931)],
            [(-94.112923,-192.732346,-71.546707),(-95.474792,-195.405411,-69.546707)],
            [(-102.145706,-209.941071,-66.677132),(-103.649414,-212.537003,-64.677132)],
            [(-120.779053,-246.512817,-57.327702),(-122.282761,-249.108749,-55.327702)],
            [(-142.149551,-286.753265,-46.477573),(-143.653259,-289.349213,-44.477573)],
            [(-149.681213,-301.973053,-39.628738),(-151.101273,-304.615662,-38.628738)],
            [(-158.236115,-319.052155,-31.887978),(-159.789108,-321.618896,-30.887978)],
            [(-168.819458,-340.385040,-22.260410),(-170.345856,-342.967682,-21.260410)],
            [(-174.568146,-352.366516,-16.893515),(-176.017502,-354.993195,-15.893515)],
            [(-189.527191,-380.918823,-6.539341),(-191.793335,-382.884674,-6.539341)],
            [(-194.283386,-398.035736,-6.738131),(-196.395493,-395.905243,-6.738131)],
            [(-207.884369,-392.555450,-7.563727),(-206.966049,-389.699463,-6.563727)],
            [(-202.641647,-374.047577,2.497336),(-201.726471,-371.190582,3.497336)],
            [(-197.336258,-356.417511,11.309425),(-198.695358,-353.743042,11.309425)],
            [(-220.870071,-337.650940,13.869003),(-222.223267,-334.973480,13.869003)],
            [(-234.272690,-311.136597,13.778691),(-235.325592,-308.327423,13.778691)],
            [(-247.712418,-287.941101,13.782051),(-247.540619,-284.946014,13.782051)],
            [(-247.712418,-287.941101,13.782051),(-245.401077,-289.853607,13.782051)],
            [(-211.451981,-312.397858,13.782275),(-209.900284,-314.965393,11.782275)],
            [(-194.673141,-310.504089,13.867300),(-195.198044,-307.550354,13.867300)],
            [(-199.999527,-279.662262,13.767035),(-200.798050,-276.770477,13.767035)],
            [(-206.489105,-263.965515,13.772101),(-208.156128,-261.471313,13.772101)],
            [(-216.976715,-238.652740,13.773614),(-216.930023,-235.653107,13.773614)],
            [(-246.905914,-257.090790,13.773846),(-246.875809,-260.090637,13.773846)],
            [(-231.600525,-247.676300,13.774094),(-232.956818,-245.000397,13.774094)],
            [(-240.579071,-229.949326,13.777535),(-241.183945,-227.010941,13.777535)],
            [(-250.084167,-189.267441,13.778445),(-251.333038,-186.539749,13.778445)],
            [(-267.735077,-148.124863,13.778445),(-269.300140,-145.565445,13.778445)],
            [(-288.454956,-115.283699,13.773356),(-291.379517,-114.615227,13.773356)],
            [(-309.651581,-107.975471,14.240871),(-312.647858,-108.124695,14.240871)],
            [(-324.993469,-107.520203,14.921846),(-327.869415,-108.374008,14.921846)],
            [(-349.915192,-115.387070,15.037639),(-346.995789,-114.696320,15.037639)],
            [(-396.287415,224.289810,17.726009),(-393.287720,224.331848,17.726009)],
            [(-386.335480,224.459656,17.758894),(-383.335785,224.501694,17.758894)],
            [(-371.324860,222.117996,17.763832),(-368.359589,221.662872,18.763832)],
            [(-340.709717,220.847214,23.200581),(-337.710052,220.803040,24.200581)],
            [(-313.383270,221.462952,26.811720),(-312.550720,218.580795,26.811720)],
            [(-313.383270,221.462952,26.811720),(-310.563721,222.487671,26.811720)],
            [(-279.815094,248.446228,26.933233),(-281.465698,250.951324,26.933233)],
            [(-295.590363,272.159668,22.991507),(-298.197296,273.644226,22.991507)],
            [(-322.250641,287.286682,17.843586),(-324.870544,288.748230,17.843586)],
            [(-356.997040,306.493103,16.482109),(-359.625519,307.939148,16.482109)],
            [(-397.215454,333.829254,8.084791),(-394.862122,331.968658,9.084791)],
            [(-377.991577,319.023712,11.614712),(-375.470947,317.396942,11.614712)],
            [(-281.229370,244.624420,26.914297),(-278.374603,245.546494,25.914297)],
            [(-243.175201,255.050690,25.932625),(-240.440048,256.283142,25.932625)],
            [(-202.424774,273.168610,20.923222),(-199.719162,274.464630,20.923222)],
            [(-187.188232,281.358429,17.446482),(-184.534470,282.757568,17.446482)],
            [(-149.466019,294.314423,15.564304),(-152.342346,293.461914,15.564304)]),
        # outside tour (added 3-29-2005)
        'tldnout':
            ([(-1028.855957,-1111.000122,223.076691),(-1027.421753,-1108.365234,222.276688)],
            [(-982.524780,-1010.501221,165.076691),(-981.360718,-1007.736267,164.376678)],
            [(-920.255554,-852.488525,139.076691),(-918.565430,-850.009949,138.376709)],
            [(-848.411133,-723.389099,115.076691),(-846.064026,-721.520691,114.476692)],
            [(-742.324402,-639.959961,98.076691),(-739.802490,-638.335205,96.276688)],
            [(-695.248413,-609.631104,93.076691),(-692.726501,-608.006348,90.676689)],
            [(-628.837646,-566.845764,61.076691),(-626.315735,-565.221008,58.076691)],
            [(-580.080383,-535.433777,-19.923309),(-577.558472,-533.809021,-20.123310)],
            [(-524.597961,-499.689026,-12.923309),(-527.050171,-501.417236,-12.693309)],
            [(-468.780212,-394.374420,-14.923309),(-467.898041,-391.507050,-14.723310)],
            [(-482.019226,-318.600830,-12.923309),(-481.427704,-315.659729,-13.573309)],
            [(-378.546448,-195.249176,20.076691),(-377.950623,-192.249527,19.676691)],
            [(-356.759949,-145.839157,20.076691),(-355.949585,-143.094162,19.676691)],
            [(-340.958954,-108.866524,20.076691),(-342.356812,-106.212097,18.476690)],
            [(-363.047089,-58.338215,-9.923309),(-363.300934,-55.348972,-10.473310)],
            [(-358.476746,-28.184626,-19.923309),(-358.730591,-25.195383,-19.873308)],
            [(-354.050568,6.651273,-11.923309),(-355.176453,9.431993,-12.323310)],
            [(-353.745361,42.171486,-20.923309),(-355.944672,43.830795,-20.523310)],
            [(-381.312836,79.945984,-17.923309),(-377.710205,80.704201,-17.223307)],
            [(-415.841431,86.699532,41.076691),(-417.339294,89.353958,40.576694)],
            [(-506.600952,174.418793,179.076691),(-504.208984,172.908203,176.926682)],
            [(-565.612488,207.042496,63.076691),(-562.613647,206.859497,61.926689)],
            [(-551.702393,457.448303,36.076691),(-549.274231,455.586517,34.926689)],
            [(-416.489288,243.764496,74.076691),(-417.331940,246.743729,72.526680)],
            [(-250.170975,809.153625,52.076691),(-250.689438,806.198792,51.976692)],
            [(-250.170975,809.153625,78.076691),(-248.930435,806.422119,77.676689)],
            [(-148.791992,534.916443,83.076691),(-147.851440,532.184937,82.246696)],
            [(-64.601593,337.129150,28.076691),(-66.773224,334.784576,27.576691)],
            [(-127.372841,264.701813,72.076691),(-126.611198,261.860107,70.576691)],
            [(26.296627,178.566849,72.076691),(23.930073,177.406601,71.476685)],
            [(-183.683380,170.267792,116.076691),(-181.477081,168.235001,114.376686)],
            [(-36.494095,86.162209,94.076691),(-36.714970,83.170349,93.076683)],
            [(-33.347755,-22.488729,94.076691),(-35.444099,-24.634735,94.076691)],
            [(20.598316,-152.538208,123.076691),(18.846371,-154.913910,121.996689)],
            [(-8.403615,-188.186722,112.076691),(-4.501012,-187.428513,111.726692)],
            [(59.928261,-177.557007,110.076691),(62.740669,-176.512802,109.126694)],
            [(104.556091,-149.251785,99.076691),(106.034439,-146.641327,97.976692)],
            [(141.284027,-88.456551,77.076691),(142.412384,-85.846092,75.776695)],
            [(167.416214,-1.576805,49.076691),(168.057098,1.353942,47.376690)],
            [(172.115921,19.915335,38.076691),(172.756805,22.846081,35.726688)],
            [(176.388382,39.453655,38.076691),(177.329285,42.384403,35.176697)],
            [(234.716309,69.487892,60.076691),(231.827423,69.545822,57.976685)],
            [(348.834320,-228.092636,36.076691),(346.936981,-224.468796,35.376686)],
            [(152.153030,-664.922058,36.076691),(152.098984,-661.937500,36.176689)],
            [(316.108978,-680.603271,333.076691),(315.258453,-677.664001,331.776703)],
            [(716.630249,786.656677,366.076691),(714.507202,784.641357,365.276703)],
            [(-328.301727,1229.852661,256.076691),(-327.823975,1226.890991,254.976715)],
            [(-633.568420,1591.158691,-4.923309),(-632.236755,1587.970337,-4.923309)]),
    },
}
# end of CameraTours

# begin of CameraShortcuts
CameraShortcuts = {
    'BaronCityOffice': {
        'scope': ['TelescopeCamera', 'TelescopeCamera.Target']
    },
    'city': {
        'scope': ['TelescopeCamera', 'TelescopeCamera.Target']
    },
    'Neighborhood': {
        'scope': ['BevinTeleCam', 'BevinTeleCam.Target']
    },
    'Teledahn': {
        'office-scope': ['telescopecamera', 'telescopecamera.Target'],
        'lbucket-scope': ['CameraTelescope', 'CameraTelescope.Target'],
        'rbucket-scope': ['TelescopeCam2', 'TelescopeCam2.Target'],
        'powertwr-scope': ['CamPwrTwrPeriscope', 'CamPwrTwrPeriscope.Target'],
    },
    'Kadish': {
        'ring1-scope': ['Scope01Cam', 'Scope01Cam.Target'],
        'ring2-scope': ['Scope02Cam', 'Scope02Cam.Target'],
        'ring3-scope': ['Scope03Cam', 'Scope03Cam.Target'],
    }
}
# end of CameraShortcuts

# begin of WarpPoints
WarpPoints = {
    'city' : {
        'abovet' : (ptPoint3(565.325562, -194.473099, 324.229309),'above the intersection near the rope bridge!',None),
        'bailout' : (ptPoint3(281.596008, 54.793194, 291.364105),'out of prison',False),
        'canopy' : (ptPoint3(430.358185, -407.610443, 309.814087),'on to the canopy near the rope bridge',None),
        'cell1' : (ptPoint3(83.843414, -92.543480, 223.681900),'into courtyard cell 1',True),
        'cell2' : (ptPoint3(74.718384, -67.901482, 221.673035),'into courtyard cell 2',True),
        'cone1' : (ptPoint3(760.343018, -669.513977, 259.250122),'inside one of the large cones near the library! Try jumping a few times!',None),
        'cone2' : (ptPoint3(773.719604, -679.034424, 259.240356),'inside one of the large cones near the library! Try jumping a few times!',None),
        'cone3' : (ptPoint3(801.131958, -714.952209, 259.246643),'inside one of the large cones near the library! Try jumping a few times!',None),
        'cone4' : (ptPoint3(828.306519, -759.860170, 259.252350),'inside one of the large cones near the library! Try jumping a few times!',None),
        'cone5' : (ptPoint3(840.757690, -769.114380, 259.253662),'inside one of the large cones near the library! Try jumping a few times!',None),
        'cone6' : (ptPoint3(872.817322, -798.097656, 259.254242),'inside one of the large cones near the library! Try jumping a few times!',None),
        'perch1' : (ptPoint3(-150.082321, -521.386108, 42.095104),'to a perch over the ferry terminal!',None),
        'perch2' : (ptPoint3(-149.372177, -542.046692, 42.086494),'to a perch over the ferry terminal!',None),
        'perch3' : (ptPoint3(-148.908310, -561.348389, 42.090477),'to a perch over the ferry terminal!',None),
        'perch4' : (ptPoint3(-149.228302, -581.074829, 42.100899),'to a perch over the ferry terminal!',None),
        'perch5' : (ptPoint3(-149.403091, -601.235718, 42.087883),'to a perch over the ferry terminal!',None),
        'galbalc' : (ptPoint3(164.929779, -445.338989, 180.305786),'to the gallery balcony',None),
        'galfloor' : (ptPoint3(154.226929, -474.471313, 160.748978),'into the gallery',None),
        'hopbar' : (ptPoint3(-143.615005, -645.962646, 8.207865),'and hopped over the barricade at the ferry terminal!',None),
        'inlibtent' : (ptPoint3(838.369324, -551.180237, 259.243530),'into the tent near the library! Setting up shop?',None),
        'intree' : (ptPoint3(0.283649, -94.167725, 220.944336),'to the tree with a hallway',None),
        'khall' : (ptPoint3(281.544586, 54.677109, 291.363861),'to the Hall of Kings',None),
        'kview' : (ptPoint3(380.223602, -172.024109, 257.977722),'to the viewpoint near the Hall of Kings',None),
        'libcol1' : (ptPoint3(854.010803, -617.131165, 290.612732),'inside a column at the library. Watch for pidegons!',None),
        'libcol2' : (ptPoint3(845.430603, -619.569092, 290.977478),'inside a column at the library. Watch for pidegons!',None),
        'libcol3' : (ptPoint3(838.121582, -626.735718, 290.984436),'inside a column at the library. Watch for pidegons!',None),
        'libcol4' : (ptPoint3(829.203369, -635.504517, 290.985089),'inside a column at the library. Watch for pidegons!',None),
        'libcol5' : (ptPoint3(820.659607, -644.025024, 290.982788),'inside a column at the library. Watch for pidegons!',None),
        'libcol6' : (ptPoint3(812.778442, -651.220459, 290.922668),'inside a column at the library. Watch for pidegons!',None),
        'libcol7' : (ptPoint3(804.918152, -658.708191, 290.986023),'inside a column at the library. Watch for pidegons!',None),
        'libtent' : (ptPoint3(839.213684, -542.252808, 275.400360),'onto the library tent',None),
        'lowfloor' : (ptPoint3(879.771118, -660.210327, 150.758423),'to the lowest library floor',True),
        'lowlib' : (ptPoint3(863.091919, -697.307861, 180.594955),'to the lower library stairs',None),
        'musin' : (ptPoint3(-208.103043, 30.606417, 225.719559),'into the museum',None),
        'musout' : (ptPoint3(-180.191635132, 19.2687950134, 221.673706055),'in front of the museum',None),
        'musorb' : (ptPoint3(-285.951355, 77.358368, 278.762726),'to see the orb at the museum!',True),
        'onstage' : (ptPoint3(-112.615479, -60.789268, 233.177917),'to the stage. No applause, just throw money!',None),
        'overpub' : (ptPoint3(-129.992157, -256.243317, 148.290573),'to a hidden area over the pub!',None),
        'pacol' : (ptPoint3(162.778809, 16.213030, 318.973328),'to the top of a column at the top of the steps near the Palace Alcove',None),
        'pole1' : (ptPoint3(-0.201223, -409.122589, 104.269569),'to the top of the guidepost on the landing above the ferry terminal! Directing traffic?',None),
        'pole2' : (ptPoint3(371.990173, -106.024918, 267.642761),'to the top of the guidepost on the landing near the Hall of Kings! Directing traffic?',None),
        'prison' : (ptPoint3(193.927322, -380.482147, 180.306931),'into the canyon prison',True),
        'rbridge' : (ptPoint3(489.007477, -306.184174, 292.371033),'to the rope bridge',None),
        'redlight' : (ptPoint3(-5.855652, 701.306274, 1501.884033),'into the red light over the city! Do not look down!',True),
        'rooftop' : (ptPoint3(89.752396, -111.080650, 254.355576,),'onto the courtyard rooftop',None),
        'rubble' : (ptPoint3(-174.508881, -475.145416, 8.214967),'into the pile of rubble at the ferry terminal!',None),
        'sled1' : (ptPoint3(786.758118, -422.022247, 295.419769),'to a sled ride near the library!',None),
        'sled2' : (ptPoint3(157.732697, 21.141609, 289.349335),'to a sled ride near the palace alcove!',None),
        'sled3' : (ptPoint3(-10.195521, -155.650085, 218.312119),'to a sled right at the top of the Great Stairs!',None),
        'sled4' : (ptPoint3(9.663712, -331.079010, 129.460789),'to a sled ride at the middle of the Great Stairs!',None),
        'sled5' : (ptPoint3(32.329823, -430.776245, 88.072220),'to a sled ride at the landing  at the base of the Great Stairs!',None),
        'sled6' : (ptPoint3(57.930038, -478.304260, 57.794056),'to a sled ride from the stairs near the ferry terminal!',None),
        'stripmall' : (ptPoint3(207.448257, -345.335144, 178.657730),'to the stripmall. Wanna go shopping?',None),
        'tentroof' : (ptPoint3(-98.520142, -119.647865, 235.182480),'on top of the tent',None),
        'tentsmash' : (ptPoint3(-99.084862, -119.690956, 1255.430832),'to the tent smash point',None),
        'tentsmashr' : (ptPoint3(-99.084862, -119.690956, 1255.430832),'to the tent smash point',False),
        'tokpil1' : (ptPoint3(-162.796631, -163.210220, 266.246521),'to the top of a pillar near Tokotah Alley',None),
        'topnxs' : (ptPoint3(857.772888, -538.943787, 266.553101),'to on top of the library Nexus terminal!',None),
        'upstairs' : (ptPoint3(415.540497, -524.310669, 289.868622),'to a hidden area above the staircase near the rope bridge!',None),
        'varch' : (ptPoint3(0.521753, -1398.257324, 220.943924),'to view the Arch!',True),
        'walkway' : (ptPoint3(865.961792, -602.898438, 271.390564),'to the walkway around the library',None),
        'trt' : (ptPoint3(-78.574852, -176.716812, 282.942627),'to Tokotah Rooftop',None),
        'trtbox' : (ptPoint3(-80.152199, -180.992599, 274.292572),'to the prison of boxes!',None),
        'trtbeam' : (ptPoint3(-165.855804, -222.436203, 146.880524),'the secret beam...',None),
        'arch10' : (ptPoint3 (50, -1719, 706), 'to visit the arch',True),
        'arch9' : (ptPoint3 (45, -1719, 706), 'to visit the arch',True),
        'arch8' : (ptPoint3 (40, -1719, 706), 'to visit the arch',True),
        'arch7' : (ptPoint3 (35, -1719, 706), 'to visit the arch',True),
        'arch6' : (ptPoint3 (30, -1719, 706), 'to visit the arch',True),
        'arch5' : (ptPoint3 (25, -1719, 706), 'to visit the arch',True),
        'arch4' : (ptPoint3 (20, -1719, 706), 'to visit the arch',True),
        'arch3' : (ptPoint3 (15, -1719, 706), 'to visit the arch',True),
        'arch2': (ptPoint3 (10, -1719, 706), 'to visit the arch',True),
        'arch1' : (ptPoint3 (0, -1719, 706), 'to visit the arch',True),
        'arch11' : (ptPoint3 (-5, -1719, 706), 'to visit the arch',True),
        'arch12' : (ptPoint3 (-10, -1719, 706), 'to visit the arch',True),
        'arch13' : (ptPoint3 (-15, -1719, 706), 'to visit the arch',True),
        'arch14' : (ptPoint3 (-20, -1719, 706), 'to visit the arch',True),
        'arch15' : (ptPoint3 (-25, -1719, 706), 'to visit the arch',True),
        'arch16' : (ptPoint3 (-30, -1719, 706), 'to visit the arch',True),
        'arch17' : (ptPoint3 (-35, -1719, 706), 'to visit the arch',True),
        'arch18' : (ptPoint3 (-40, -1719, 706), 'to visit the arch',True),
        'arch19' : (ptPoint3 (-45, -1719, 706), 'to visit the arch',True),
        'arch20' : (ptPoint3 (-50, -1719, 706), 'to visit the arch',True),
        'tourd' : (ptPoint3 (0, -146.229141, 222.945648), 'to the end of the tour',False),
        'fetop' : (ptPoint3 (-215.812055, -446.882813, 69.008926), 'to the top of the ferry terminal',None),
        'hide1' : (ptPoint3 (-170.189850, -431.248657, 8.215761), 'to a hiding place!',None),
        'spyroom' : (ptPoint3(-139.5,-138.9,256.7), 'to a spyroom',True)
    },

    'Cleft' : {
        'bedrm' : (ptPoint3(375.049774, 128.544937, -8.855470),'into the bedroom',None),
        'bird1' : (ptPoint3(-259.724670, 300.293152, 60.004913),'to view a bird!',True),
        'bird2' : (ptPoint3(-259.724670, 289.293152, 59.004913),'to view a bird fly through you!',True),
        'bones1' : (ptPoint3(-79.720352, 341.178619, 9.906741),'on top of a pile of bones',None),
        'bones2' : (ptPoint3(-69.183083, 334.770721, 8.514209),'on top of a pile of bones',None),
        'bones3' : (ptPoint3(-62.411236, 328.848236, 8.507324),'on top of a pile of bones',None),
        'bones4' : (ptPoint3(-56.635384, 321.695435, 8.511662),'on top of a pile of bones',None),
        'bookrm' : (ptPoint3(481.092401, 97.458504, -36.692448),'to the Relto book cave',None),
        'bucket' : (ptPoint3(435.740417, 89.743324, -23.442102),'into the bucket in the cleft. Going up?',None),
        'dive' : (ptPoint3(446.613739, 87.005974, 11.701668),'to the edge of the cleft. Dive on in!',None),
        'edge' : (ptPoint3(4853.593750, -815.024536, 0.005865),'to the edge of the world. Hmm... flat after all?',None),
        'high1' : (ptPoint3(108.251465, 74.387375, 225.867493),'to a high viewpoint!',True),
        'high2' : (ptPoint3(113.251465, 79.387375, 225.867493),'to a high viewpoint!',True),
        'high3' : (ptPoint3(108.251465, 84.387375, 225.867493),'to a high viewpoint!',True),
        'high4' : (ptPoint3(103.251465, 79.387375, 225.867493),'to a high viewpoint!',True),
        'hop1' : (ptPoint3(291.694977, 133.298477, 37.079117),'over the fence at the volcano',None),
        'hop2' : (ptPoint3(115.443687, 463.752838, 3.862479),'over the fence surrounding the cleft',None),
        'incleft' : (ptPoint3(425.254700, 88.447372, -29.341821),'into the cleft',None),
        'intrail' : (ptPoint3(465.235565, -45.861942, 1.265521),'to inside of the trailer',None),
        'jcrm1' : (ptPoint3(361.260437, 79.305832, -7.120074),'into the kitchen',None),
        'jcrm2' : (ptPoint3(359.287170, 126.126373, -8.758240),'into the small room with the journey cloth',None),
        'junk' : (ptPoint3(165.886566, 390.655548, 14.077095),'to a pile of junk from Riven',None),
        'ladder' : (ptPoint3(410.626617, 103.478500, -1.132778),'to the base of the ladder in the cleft',None),
        'lever' : (ptPoint3(390.810516, 74.257057, -11.347351),'into the room with the lever',None),
        'ontrail' : (ptPoint3(465.235565, -43.488651, 18.240427),'to over the top of the trailer',None),
        'potsrm' : (ptPoint3(428.351807, 105.846397, -17.289112),'into the small room with the pottery',None),
        'soak' : (ptPoint3(425.527161, 88.474388, -33.641972),'into the cleft pool to soak for a few. Hot desert out there!',None),
        'upbkt' : (ptPoint3(437.125092, 95.060455, -10.404575),'to the small ledge over the bucket',None),
        'windmill' : (ptPoint3(381.251465, 74.387375, 32.112938),'to the top of the windmill!',None),
        'zandoni' : (ptPoint3(-1289.500977, -2046.202271, 0.030862),'to the Zandoni',None),
    },

    'Garrison' : {
        'gabado' : (ptPoint3(151.678497, -326.501068, 10022.075195),'to the Bahro Cave door',None),
        'gabconf' : (ptPoint3(-76.791443, 209.711594, 0.006031),'into the conference room with the blue notebook on the table',None),
        'gabconft' : (ptPoint3(-86.4666110, 219.508011, 0.003461),'inside the conference table with the blue notebook!',None),
        'gabeam' : (ptPoint3(23.355104, 447.221680, 1039.641602),'to the top of a beam at the top of the Maintainer Training Center!',None),
        'gacell' : (ptPoint3(73.444542, 442.196136, 965.732910),'the prison cell above the Maintainer Training Center',None),
        'gagconf' : (ptPoint3(70.931313, 140.339828, 0.003253),'into the conference room with the green notebook on the table',None),
        'gagconft' : (ptPoint3(86.694939, 134.470749, 0.000103),'inside the conference table with the green notebook!',None),
        'gahall' : (ptPoint3(-88.596077, 14.531943, 3.006263),'to the hallway in the Maintainer Training Center',None),
        'gakirm' : (ptPoint3(71.169136, 530.571899, 965.747192),'to the KI machine room above the Maintainer Traning Center',None),
        'gamesa1' : (ptPoint3(71.964241, -265.237701, 10085.708984),'to Upper Gahreesen Mesa',None),
        'gamesa2' : (ptPoint3(-110.269165, -611.761169, 10068.324219),'to Lower Gahreesen Mesa',None),
        'gamesa3' : (ptPoint3(121.476936, -251.785828, 10066.562500),'to Middle Gahreesen Mesa',None),
        'ganxs' : (ptPoint3(67.253059, -448.701080, -278.898346),'to the Gahreesen Nexus',None),
        'gapnxs' : (ptPoint3(-376.560150, -0.123376, 0.004436),'to the purple Maintainer Nexus',None),
        'gaplank' : (ptPoint3(117.476852, -459.807037, -250.171143),'the plank! Arrrg, ye be careful while walking it!',None),
        'gapower' : (ptPoint3(28.691118, -504.541473, -250.511353),'into the power room!',None),
        'gappan'  : (ptPoint3(2.715042, 250.801239, 0.010558),'into the purple control room',None),
        'gaprm' : (ptPoint3(-35.506039, 218.742279, -28.073416),'into the purple wallclimbing room',None),
        'gatop' : (ptPoint3(70.472588, 530.601257, 1005.574219),'to the top of the Maintainer Training Center building. Nice view!',None),
        'gatop1' : (ptPoint3(63.067154, 461.031982, 1026.337036),'to the top of an object at the top of the Maintainer Training Center!',None),
        'gatop2' : (ptPoint3(71.295197, 461.014374, 1026.337036),'to the top of an object at the top of the Maintainer Training Center!',None),
        'gatop3' : (ptPoint3(79.067154, 461.031982, 1026.337036),'to the top of an object at the top of the Maintainer Training Center!',None),
        'gaunmtc' : (ptPoint3(-113.114372, 493.525940, 10042.458008),'to the base on the underside of the Maintainer Training Center!',None),
        'gaynxs' : (ptPoint3(-470.356781,-0.123376,0.010404),'to the yellow Maintainer Nexus',None),
        'gaypan' : (ptPoint3(-3.380678, 100.086571, 0.001650),'into the yellow control room',None),
        'gayrm' : (ptPoint3(-33.353241, 131.224731, -28.295019),'into the yellow wallclimbing room',None),
    },

    'Gira' : {
        'gi86' : (ptPoint3(-78.574852, -176.716812, 282.942627),'out the hard way!',None),
        'giarch1' : (ptPoint3(55.004307, -63.029907, -9.424695),'on top of the bone arch, position 1',None),
        'giarch2' : (ptPoint3(56.910511, -62.291504, -9.081109),'on top of the bone arch, position 2',None),
        'giarch3' : (ptPoint3(59.336006, -61.709671, 10.167565),'on top of the bone arch, position 3',None),
        'giarch4' : (ptPoint3(63.238136, -60.694012, -12.736801),'on top of the bone arch, position 4',None),
        'gibird1' : (ptPoint3(84.721603, 47.135193, 156.229889),'to see the bird!',True),
        'gibird2' : (ptPoint3(106.721603, -152.864087, -8.770111),'to see the bird!',True),
        'giblock' : (ptPoint3(44.175072, 58.597710, -14.292088),'on top of the block',None),
        'gibone' : (ptPoint3(90.567970, -9.196574, -14.037334),'to the top of the bone',None),
        'gicave' : (ptPoint3(70.639580, 52.810539, -4.115467),'into the cave',None),
        'gidrop' : (ptPoint3(17.810442, 68.834251, -14.721561),'over the rock wall',None),
        'gifalls' : (ptPoint3(137.591400, -46.251499, 12.605422),'to the top of the falls! Watch your step!',None),
        'gifloat' : (ptPoint3(20.463236, -33.470062, -4.085382),'while inhaling helium again',True),
        'gijcled1' : (ptPoint3(-39.610325, -25.108400, 5.932511),'to the lower ledge, watch yer step there!',None),
        'gijcled2' : (ptPoint3(-79.518677, -25.414640, 28.435789),'to the upper ledge',None),
        'gilavaisle' : (ptPoint3(-22.673435, -27.026466, -17.763561),'to an uncharted desert isle',None),
        'ginxs' : (ptPoint3(-83.908775, 18.374470, 1.733501),'to Eder Gira Nexus',None),
        'gipool' : (ptPoint3(118.897255, -14.215436, -1.135948),'to the pool, splish splash you are taking a bath',None),
        'gipoolr' : (ptPoint3(118.897255, -14.215436, -1.135948),'to the pool, splish splash you are taking a bath',False),
        'gistone' : (ptPoint3(89.309494, -49.787968, -17.957739),'to the rock, rock on d00d!',None),
        'gisun' : (ptPoint3(-0.278393, 302.135193, 266.229889),'into the path of the sun! Has to be the right time of day for a good view!',True),
    },

    'GreatZero' : {
        'grz' : (ptPoint3(-0.109616, -36.897400, -40.054607),'into the Great Zero',None),
        'grzo' : (ptPoint3(-0.146269, -127.644348, 9.817596),'into the Great Zero Observatory',None),
        'grzm' : (ptPoint3(0.218273, 291.001251, -11.342631),'into the Great Zero marker mission room',None),
        'grznxs' : (ptPoint3(-29.112467, -66.555138, -16.963856),'to the Great Zero Nexus book',None),
        'gzo' : (ptPoint3(0,-128, 10),'to the GZO',True),
        'gzuny' : (ptPoint3(0, -500, 0),'out of the GZ into the middle of nowhere',True),
        'gzplusy' : (ptPoint3(0, 1000, 0),'thru the GZ and out other side',True),
        'gzhibeam' : (ptPoint3(0, 700, 160),'to a high overall view on beamline',True),
        'gzpwrin' : (ptPoint3(0, 499, 60),'to center back power input pillar',True),
        'gzbeamorig' : (ptPoint3(0, 480, -19),'to the beam origin',True),
        'gzlowbeam' : (ptPoint3(0, 480, -22),'near beam origin',True),
        'gztopw1' : (ptPoint3(0, 120, -23),'to the top of waterfall 1',True),
        'gzbotw1' : (ptPoint3(0, 96, -28),'to the bottom of waterfall 1',True),
        'gztween' : (ptPoint3(0, 90, -22),'between the steering xtals',True),
        'gzbotw2' : (ptPoint3(0, 39, -43),'to the bottom of waterfall 2',True),
        'gzgurgle' : (ptPoint3(0, 29, -46),'deep in water before whirly',True),
        'gzflush' : (ptPoint3(0, 5, -44),'center of whirlpool (flushed)',True),
        'gzin' : (ptPoint3(0, 0, -23),'middle of main xtal',True),
        'gzzero' : (ptPoint3(0, 0, 0),'the center of the universe! position 0 0 0',True),
        'gz000' : (ptPoint3(0, 0, 0),'the center of the universe! position 0 0 0',True),
        'gzcambeam' : (ptPoint3(0, 30, 3),'to where the camera gets the GZ beamage',True),
        'gzemit' : (ptPoint3(0, 50, 15),'to the GZ beam emitter',True),
        'gztopof' : (ptPoint3(0, 0, 15),'just above the main xtal, feel the power!',True),
        'gzroll' : (ptPoint3(0, 25, 12),'into the path of the spinning avvie roller',True),
        'gzthump' : (ptPoint3(0, 13, 12),'to the avvie thumper position',True),
        'gzring' : (ptPoint3(0, 10, 28),'to the ring job',True),
        'gzgizmo' : (ptPoint3(0, 50, 28),'to a GZ gizmo view',True),
        'gzsmisle' : (ptPoint3(-78, 534, -16),'to a small island by input pillars',True),
        'gzipillars' : (ptPoint3(-60, 500, -16),'for a side view of input pillars',True),
        'gzmidlake' : (ptPoint3(-100, 450, 33),'to a mid high side view of beam over lake',True),
        'gzlake' : (ptPoint3(-100, 400, 0),'to a lake view of beam',True),
        'gzwindow' : (ptPoint3(0, 340, 0),'to top of beam input window by marker machines',True),
        'gzpool' : (ptPoint3(0, 320, -29),', now standing on bottom of pool by marker machines',True),
        'gzimager' : (ptPoint3(0, 214, 30),'somewhere between arch thingys above imager room',True),
    },

    'Kadish' : {
        'kabado' : (ptPoint3(990.372437, 51.9922340, -72.719177),'to the Bahro Cave door',None),
        'kabeam' : (ptPoint3(1098.710083, 197.742950, -10.908210),'to one of the support beams for Kadish Vault! Watch yer step there!',None),
        'kajcsteps' : (ptPoint3(817.206421, -9.411834, -85.449837),'to the pillar steps',None),
        'kaptop' : (ptPoint3(794.723083, -26.831114, 89.155663),'to the top of the highest pillar',None),
        'kalevers' : (ptPoint3(772.517395, -43.624332, -136.638214),'to the pillar levers',None),
        'kalow' : (ptPoint3(313.018188, 107.977135, 0.008306),'to the  lower lock control',None),
        'kalowv' : (ptPoint3(309.687469, 103.814072, 11.773027),'to the top of the lower lock viewer',None),
        'kamid' : (ptPoint3(165.493668, 232.376175, 15.567680),'to the middle lock control',None),
        'kamidv' : (ptPoint3(168.704041, 229.129318, 21.691412),'to the top of the middle lock viewer',None),
        'kamidin' : (ptPoint3(210.264999, 191.763077, 9.998847),'inside the middle lock mechanism!',None),
        'kanxs' : (ptPoint3(123.232773, 23.249447, 0.101166),'to Kadish Nexus book',None),
        'kapytop' : (ptPoint3(732.474976, -115.531288, 2.057676),'to the top of the pyramid!',None),
        'kaup' : (ptPoint3(50.148422, 181.381393, 14.463024),'to the upper lock control',None),
        'kaupv' : (ptPoint3(59.742702, 189.346939, 21.253262),'to the top of the upper lock viewer',None),
        'kavault' : (ptPoint3(1179.269287, 209.614761, 8.351727),'to Kadish Vault',None),
        'kaview1' : (ptPoint3(473.121613, -253.592209, -64.645287),'to Kadish viewpoint 1',None),
        'kaview2' : (ptPoint3(553.942322, -299.798767, -64.477020),'to Kadish viewpoint 2',None),
    },

    'Garden' : {
        'kebado' : (ptPoint3(-62.314785, 171.302826, -9.814954),'to the Bahro Cave door',None),
        'kelink' : (ptPoint3(285.641968, 7.556997, -17.945719),'to the linking book for Eder Gira',None),
        'kepl1' : (ptPoint3(82.330925, -41.132378, -1.526413),'on top of a plant',None),
        'kepl2' : (ptPoint3(78.403221, -32.171501, 1.526413),'on top of a plant',None),
        'kerpl' : (ptPoint3(96.969528, -32.830870, -4.964595),'to the Relto page ledge',None),
        'ketot1' : (ptPoint3(-74.448929, 43.385098, 8.221173),'to the top of the tunnel!',None),
        'ketot2' : (ptPoint3(169.190979, -47.519951, -7.967232),'to the top of the tunnel!',None),
        'ketree1' : (ptPoint3(59.450554, 92.903748, -3.925620),'to the tree!',None),
        'ketree2' : (ptPoint3(69.049149, 107.927010, -7.628707),'to the tree!',None),
        'ketree3' : (ptPoint3(88.913956, 97.246147, -5.573625),'to the tree!',None),
        'ketree4' : (ptPoint3(-45.652767, 168.389282, -6.087781),'to the tree!',None),
        'ketree5' : (ptPoint3(-70.788261, 156.514130, -6.388485),'to the tree!',None),
        'ketree6' : (ptPoint3(-32.972301, 144.820007, -6.611439),'to the tree!',None),
        'kefount' : (ptPoint3(133.547195, 97.625732, 15.287938),'to the top of the fountian!',None),
    },

    'Neighborhood' : {
        'camera' : (ptPoint3(256.085327, -813.994385, 8.537565),'to on top of the camcorder. Hey! You are on-camera!',None),
        'classroof' : (ptPoint3(71.814521789550781, -819.35284423828125, 27.022296905517578),'to the classroom roof',None),
        'eggroom' : (ptPoint3(29.791488647460938, -776.909423828125, 8.1029748916625977),'into the eggroom',None),
        'gardlook' : (ptPoint3(125.83461761474609, -831.38592529296875, 29.52827262878418),'to the garden overlook',None),
        'grlamp1' : (ptPoint3(150.166473, -885.310242, -8.552455),'to the top of a green lamp!',None),
        'grlamp2' : (ptPoint3(150.495758, -861.980896, -8.254499),'to the top of a green lamp!',None),
        'grlamp3' : (ptPoint3(174.838837, -893.250732, -8.196931),'to the top of a green lamp!',None),
        'grlamp4' : (ptPoint3(112.316309, -885.901428, -8.642586),'to the top of a green post!',None),
        'grlamp5' : (ptPoint3(121.793526, -926.639282, -8.559774),'to the top of a green lamp!',None),
        'hrpost' : (ptPoint3(247.223389, -769.268921, 14.250823),'to the top of the handrail post!',None),
        'linkroom' : (ptPoint3(127.430321, -766.592529, 9.428532),'into the linkroom',None),
        'nbalc' : (ptPoint3(28.973207473754883, -798.04461669921875, 78.954200744628906),'to the neighborhood balcony',None),
        'nhide1' : (ptPoint3(182.225052, -794.280579, 1.077279),'to a hiding place!',None),
        'orlamp1' : (ptPoint3(138.210901, -884.389465, 4.014853),'to the top of a orange lamp!',None),
        'orlamp2' : (ptPoint3(119.355476, -905.191711, 3.995540),'to the top of a orange lamp!',None),
        'orlamp3' : (ptPoint3(149.019897, -905.079468, 4.010039),'to the top of a orange lamp!',None),
        'spyroom' : (ptPoint3(225.310608, -794.448368, 12.566200),'into the spyroom. Sneaky...',None),
    },

    'Personal' : {
        'behind1' : (ptPoint3(70.202871, 46.702518, 9.650284),'to behind the trees. Watch your step!',None),
        'behind2' : (ptPoint3(89.992325, 32.716873, 5.855053),'to backside of Relto Island. Watch your step!',None),
        'gohome' : (ptPoint3(74.018631, -13.603501, 19.887648),'to Relto Island!',None),
        'isle1' : (ptPoint3(-70.503059, 112.103546, 2.561520),'to the tree island!',None),
        'isle2' : (ptPoint3(-87.493103, 77.718834, 2.479377),'to the far island!',None),
        'isle3' : (ptPoint3(-56.489334, -23.159721, 6.692364),'to the large island',None),
        'isle4' : (ptPoint3(-45.503059, 69.103546, 5.115726),'to an island!',None),
        'isle5' : (ptPoint3(-28.503059, 69.103546, 5.390036),'to an island!',None),
        'isle6' : (ptPoint3(-33.503059, 53.103546, 4.886618),'to an island!',None),
        'isle7' : (ptPoint3(-17.503910, 39.514175, 2.481721),'to an island!',None),
        'isle8' : (ptPoint3(2.496090, 61.514175, 4.702849),'to an island!',None),
        'isle9' : (ptPoint3(20.496090, 69.514175, 2.536776),'to an island!',None),
        'isle10' : (ptPoint3(22.496090, 53.514175, 2.481141),'to an island!',None),
        'isle11' : (ptPoint3(35.496090, 55.514175, 3.518473),'to an island!',None),
        'isle12' : (ptPoint3(-63.461639, 45.450813, -2.893143),'to the foggy island!',None),
        'topmt' : (ptPoint3(75.657204, 15.767704, 58.866127),'to the top of the world! This one, anyway...',None),
        'tree' : (ptPoint3(6.633122, -20.327078, 32.290192),'to the top of big tree',None),
        'imager' : (ptPoint3(48.394287, -26.596539, 15.522755),'on top of the imager',None),
        'clock' : (ptPoint3(-62.457077, -61.582504, 6.897969),'to the clock island',None),
    },

    'Teledahn' : {
        'tebado' : (ptPoint3(-308.891602, 211.725998, 22.039608),'to the Bahro Cave door!',None),
        'tebrknbkt' : (ptPoint3(-109.525642, -208.464096, 88.363556),'to the top of the broken bucket in the control room!',None),
        'tednoff' : (ptPoint3(-413.305969, 238.343613, 3.228420),'to the lower room',None),
        'tedock' : (ptPoint3(-479.901245, -286.374664, -24.582552),'to the stranded dock',None),
        'tedrop' : (ptPoint3(-52.820381, -191.977158, 82.683395),'to the bucket drop off',None),
        'tefd1' : (ptPoint3(-361.712158, 24.266533, -24.562963),'to the Shroomie feeder by the drawbridge',None),
        'tefd2' : (ptPoint3(-474.904266, 414.706421, -23.111019),'to the Shroomie feeder by the nailgun',None),
        'tefdt' : (ptPoint3(-481.376465, 419.226471, -6.001920),'to the top of the Shroomie feeder by the nailgun!',None),
        'tefish' : (ptPoint3(-99.908958, -206.669113, 131.423080),'inside the fish tank!',None),
        'tegate' : (ptPoint3(-138.29100, 299.536224, 5.832080),'to the water gate. Watergate?!',None),
        'tegear' : (ptPoint3(-481.494415, 418.865906, -23.254074),'inside the gears of Shroomie feeder 2. Need to grind up some chum?',True),
        'teglass1' : (ptPoint3(339.799805, -211.212555, 25.099604),'to a mushroom with a wineglass on it!',True),
        'teglass2' : (ptPoint3(178.802521, 54.963531, 32.025169),'to a mushroom with a wineglass on it!',True),
        'tegun' : (ptPoint3(-445.285980, 363.876160, -2.151910),'to the gun! Blast away!!',None),
        'tehide1' : (ptPoint3(-64.552147, -172.983398, 71.798526),'to the hiding place!',None),
        'tehide2' : (ptPoint3(-64.366852, -192.189621, 71.804855),'to the hiding place!',None),
        'teisle' : (ptPoint3(296.033813, -23.308323, 4.783095),'to the island top',None),
        'temush' : (ptPoint3(-0.015733, 0.041178, 0.012677),'to the underside of a mushroom! Turn to look, but do not move or you will fall!',None),
        'tenxs' : (ptPoint3(-105.348465, -217.584045, 131.514618),'to the Teledahn Nexus',None),
        'tepan' : (ptPoint3(-96.120590, -211.333282, 80.745819),'to the control room',None),
        'tepeep' : (ptPoint3(-120.558861, -135.030029, 83.596016),'to where you are looking into the control room window. Peeping Tom!',True),
        'tepri' : (ptPoint3(-219.345123, -311.468597, 8.767313),'to the prison holding cell',None),
        'teprisw' : (ptPoint3(-216.745056, -234.088272, 8.769681),'to the prison cell switches',None),
        'teroof' : (ptPoint3(-86.260658, -181.089767, 27.388273),'to the top of the hut!',None),
        'teswim1' : (ptPoint3(-461.242096, 458.602509, -37.057571),'into the the water near Shroomie feeder 2! Time to cool off?',True),
        'teswim2' : (ptPoint3(-465.242096, 458.602509, -37.057571),'into the the water near Shroomie feeder 2! Time to cool off?',True),
        'teswim3' : (ptPoint3(-469.242096, 458.602509, -37.057571),'into the the water near Shroomie feeder 2! Time to cool off?',True),
        'teswim4' : (ptPoint3(-473.242096, 458.602509, -37.057571),'into the the water near Shroomie feeder 2! Time to cool off?',True),
        'teunder' : (ptPoint3(-119.856949, -194.123260, 71.775787),'under the floor of the control room!',None),
        'teupoff' : (ptPoint3(-409.446045, 240.656769, 29.388769),'to the upper room',None),
    },

    'Ercana' : {
        'carstart' : (ptPoint3(-878.34753418, -682.286437988, -49.823764801),'to the start position of the harvester',None),
        'controlrm' : (ptPoint3(-0.061584, 375.992645, 52.451714),'to the control room',None),
        'pellets' : (ptPoint3(0.368883, 750.199646, 79.055595),'to the pellet dispenser',None),
        'marbles' : (ptPoint3(-97.034714, 344.680603, 51.901104),'to the firemarble page',None),
        'backpool' : (ptPoint3(-411.596710205, -554.542602539, -38.3305625916),'to the pool by the clue',None),
        'fissure' : (ptPoint3(-281.95526123, -959.629272461, -33.676410675),'to the fissure drawing',None),
        'archtop' : (ptPoint3(-126.762771606, -784.956542969, 59.7312355042),'to the top of the arch',None),
        'inarch' : (ptPoint3(-123.931533813, -782.908630371, -6.88972997665),'inside the arch', None),
        'onpoint' : (ptPoint3(-341.195587158, -811.250305176, 1.08038794994),'to the ridge point',None),
        # surprise! solid, note, all easy to fall from
        'tinyledge' : (ptPoint3(-195.99307251, -85.5243835449, 117.807815552),'to a small ledge',None),
        'building' : (ptPoint3(-202.657928467, -100.781730652, 90.7803268433),'to part of the side building',None),
        'hollow' : (ptPoint3(-164.878036499, -149.338180542, -25.9250259399),'to a walled-in spot',None),
    },

    'AhnySphere01' : {
        'intower' : (ptPoint3(179.377731, 109.751625, 18.324200),'inside the tower',None),
        'diving' : (ptPoint3(-1.000000, -2.000000, 61.739330),'to the top of the clock',None),
        'swimrock1' : (ptPoint3(37.524200, 39.811935, 4.625159),'to a rock',None),
        'swimrock2' : (ptPoint3(-21.424164, -14.549045, 2.372455),'to a rock',None),
        'viewrock1' : (ptPoint3(-272.160980, 84.052589, 38.477154),'to a faraway rock',None),
        'viewrock2' : (ptPoint3(231.396393, 62.733803, 19.949497),'to a rock near the tower',None),
        'towertop' : (ptPoint3(183.130646, 113.435280, 67.761818),'to the top of the tower',None),
        'screen1' : (ptPoint3(-124.609665, -393.051910, 91.559898),'to the front screen',None),
        'screen2' : (ptPoint3(0.149239, 412.364288, 91.572952),'to the balance beam, I mean screen',None),
    },

    'AhnySphere04' : {
        'sparks' : (ptPoint3(-4.372056, 532.538696, 67.181984),"to the sparks",None),
        'enghut' : (ptPoint3(-856.478760, -1254.193481, 9764.611328),"to inside the engineer's hut",None),
        'engdoor' : (ptPoint3(-871.117554, -1235.823853, 9761.194336),"to outside the engineer's hut",None),
        'intower' : (ptPoint3(164.398544, 104.384377, 87.909859),'inside the tower',None),
        'uptower' : (ptPoint3(159.726196, 105.239044, 101.077225),'partway up the tower',None),
        'insideball' : (ptPoint3(-57.970665, 7.722978, 188.815369),'inside the ball, make sure to look down!',True),
    },
}
# end of WarpPoints

# begin of ObjectLists
ObjectLists = {
    'BahroCave': {
        'yellow' : ('RedParentBox','RTomniRedWalls','RtWedgeOmniRed','RTomniRed01','RTomniRed02','RTomniRed03','RTomniRed04','RTomniRed05','RTomniRed06','FireGlareRed01','FireGlareRed02','FireGlareRed03','FireGlareRed04','FireGlareRed05','FlamerRed01','FlamerRed02','FlamerRed03','FlamerRed04','FlamerRed05','LightLampRed01','LightLampRed02','LightLampRed03','LightLampRed04'),
        'blue' : ('BlueParentBox','RTOmniLighFlameWalls','RTWedgesOmniLight01','RTOmniLighFlame','RTOmniLighFlame01','RTOmniLighFlame02','RTOmniLighFlame03','RTOmniLighFlame04','RTOmniLighFlameAVATAR','FireGlare','FireGlare01','FireGlare02','FireGlare03','FireGlare04','Flamer','Flamer01','Flamer02','Flamer03','Flamer04','LampLighta','LampLightb','LampLightc','LightLampd'),
        'floor' : ('Wedge-Garden','Wedge-Garrison','Wedge-Kadish','Wedge-Teledahn'),
        'walls' : ('CaveWall','CaveWallUnderneath'),
        'stars' : ('Starfield01','Starfield02'),
        'water' : ('CityWater01',),
        #  The sparks that fall when the hand is pressed
        'polesparks' : ('Pole_TeledahnParticle','Pole_TeledahnParticle02','Pole_KadishParticle01','Pole_KadishParticle02','Pole_GarrisonParticle01','Pole_GarrisonParticle02','Pole_GARDENParticle01','Pole_GardenParticle02'),
        #  The smoke from the pots (both caves)
        'smoke' : ('SmokerUp','SmokerUp01','SmokerUp02','SmokerUp03','SmokerUp04','SmokerUpRed','SmokerUpRedSmall01','SmokerUpRedSmall02','SmokerUpRedSmall03','SmokerUpRedSmall04'),
        #  The dust falling from the pots (both caves)
        'dust' : ('Duster','Duster01','Duster02','Duster03','Duster04','Duster05','Duster06','Duster07','Duster08','Duster09','Duster01Red','DusterRed','DusterRedSmaller01','DusterRedSmaller02','DusterRedSmaller03','DusterRedSmaller04','DusterRedSmallest01','DusterRedSmallest02','DusterRedSmallest03','DusterRedSmallest04'),
        #  Blue cave smoke
        'bsmoke' : ('SmokerUp','SmokerUp01','SmokerUp02','SmokerUp03','SmokerUp04'),
        #  Blue cave dust
        'bdust' : ('Duster','Duster01','Duster02','Duster03','Duster04','Duster05','Duster06','Duster07','Duster08','Duster09'),
        #  Yellow cave smoke
        'ysmoke' : ('SmokerUpRed','SmokerUpRedSmall01','SmokerUpRedSmall02','SmokerUpRedSmall03','SmokerUpRedSmall04'),
        #  The base which supports the bahro poles
        'polebase' : ('YeeshaPolePedestal-Garden','YeeshaPolePedestal-Garrison','YeeshaPolePedestal-Kadish','YeeshaPolePedestal-Teledahn','PoleDecal-Garden','PoleDecal-Garrison','PoleDecal-Kadish','PoleDecal-Teledahn'),
        #  Hand symbols on walls
        'hand' : ('HandDecal01','HandDecal02','HandDecal03','HandDecal04'),
        # Hand symbols on walls glowing
        'handglow' : ('JC05BahroPalmGlow10','JC05BahroPalmGlow11','JC05BahroPalmGlow12','JC05BahroPalmGlow13'),
        #  Yeesha drawings on walls
        'drawing' : ('YeeshaDec01_Kdsh','YeeshaDec02_Grsn','YeeshaDec03_Tldn','YeeshaDec04_Grdn'),
        #  The glowing Yeesha drawings
        'decalglow' : ('YeeshaDec01Glow_Kdsh','YeeshaDec02Glow_Grsn','YeeshaDec03Glow_Tldn','YeeshaDec04Glow_Grdn'),
        #  Islands below cave
        'islands' : ('IslandA01','IslandA02','IslandA03','IslandA04','IslandA05','IslandA06','IslandA07','IslandA08','IslandB01','IslandB02','IslandB03','IslandB04','IslandB05','IslandB06','IslandB07','IslandB01','WaterGlow01','WaterGlow02','WaterGlow03','WaterGlow04','WaterGlow05','WaterGlow06','WaterGlow07','WaterGlow08','WaterGlow09','WaterGlow10','WaterGlow11','WaterGlow12','WaterGlow13','WaterGlow14','WaterGlow15','WaterGlow16'),
        #  All flame pots and ropes
        'fixtures' : ('Light','Light01','Light02','Light03','Light04','Rope','Rope01','Rope02','Rope03','Rope04','RopeTieStick','RopeTieStick01','RopeTieStick02','RopeTieStick03','Light Tusk','Light Tusk01','Light Tusk02','Light Tusk03','Light Support','Light Support01','Light Support02','Light Support03','Light Support04'),
        #  All tusks including bahro pole tusks
        'tusks' : ('Tusk01','Tusk02','Tusk03','Tusk04','Tusk05','Tusk06','Tusk07','Tusk08','Tusk09','Tusk10','Tusk11','TuskShad','TuskShad01','TuskShad01a','TushShad02a','TushShad03a','TuskShad02','TuskShad03','TuskShad04','TuskShad05','TuskShad06','TuskShad07','TuskShad08','TuskShad09','TuskShad10','TuskShad11','TuskShad12','TuskShad13','TuskShad14','TuskShad15','TuskShad16','TuskShad17','Wall Tusk01','Wall Tusk02','Wall Tusk03','Wall Tusk04','Wall Tusk05','Wall Tusk06','Wall Tusk07','Wall Tusk08','Wall Tusk09','Wall Tusk10','Wall Tusk11','Wall Tusk12','Wall Tusk13','Wall Tusk14','Wall Tusk15','Wall Tusk16','Wall Tusk17','Wall Tusk01a','Wall Tusk02a','Wall Tusk03a','Wall Tusk04a','Wall Tusk05a','Wall Tusk06a','Wall Tusk07a','Wall Tusk08a','Wall Tusk09a','Wall Tusk10a','Wall Tusk11a','Wall Tusk12a','Wall Tusk13a','Wall Tusk14a','Wall Tusk15a','Wall Tusk16a','Wall Tusk17'),
        #  The bahro poles
        'poles' : ('Pole_Garden','Pole_Garrison','Pole_Kadish','Pole_Teledahn'),
        #  Yellow light
        'ylight' : ('LightLampRed01','LightLampRed02','LightLampRed03','LightLampRed04'),
        #  Blue light
        'blight' : ('LampLighta','LampLightb','LampLightc','LightLampd'),
        #  The blue glow from the poles
        'poleglow' : ('Pole_GardenBlue','Pole_GarrisonBlue','Pole_KadishBlue','Pole_TeledahnBlue'),
        #  The flicker of the blue flames
        'bflicker' : ('RTOmniLighFlame','RTOmniLighFlame01','RTOmniLighFlame02','RTOmniLighFlame03','RTOmniLighFlame04'),
        #  The flicker of the yellow flames
        'yflicker' : ('RTomniRed01','RTomniRed02','RTomniRed03','RTomniRed04','RTomniRed05','RTomniRed06'),
        #  Blue cave flames
        'bflame' : ('Flamer','Flamer01','Flamer02','Flamer03','Flamer04'),
        #  Yellow cave flames
        'yflame' : ('FlamerRed01','FlamerRed02','FlamerRed03','FlamerRed04','FlamerRed05'),
        #  Glare from blue cave flames
        'bfire' : ('FireGlare','FireGlare01','FireGlare02','FireGlare03','FireGlare04'),
        #  Glare from yellow cave flames
        'yfire' : ('FireGlareRed01','FireGlareRed02','FireGlareRed03','FireGlareRed04','FireGlareRed05'),
        'cafesafe' : ('LinkOutRgn'),
    },

    'city' : {
        'citycones' : ('OrangeCone','OrangeCone01','OrangeCone02','OrangeCone03','OrangeCone04','OrangeCone05','OrangeCone06','OrangeCone06b','OrangeCone07','OrangeCone07b','OrangeCone08','OrangeCone08b','OrangeCone09','OrangeCone09b','OrangeCone10','OrangeCone10b','OrangeCone11','OrangeCone11b','OrangeCone12','OrangeCone18','OrangeCone19','ALYOrangeCone10','ALYOrangeCone11','ALYOrangeCone12','ALYOrangeCone13'),
        'citycones2' : ('OrangeCone13','OrangeCone14','OrangeCone15','OrangeCone16','OrangeCone17','OrangeCone20','OrangeConeL18','OrangeConeL19','OrangeConeL20','OrangeConeL21','OrangeConeL22','OrangeConeL23','OrangeConeL24','ALYOrangeCone09'),
        'lights' : ('RTOmniLight01','RTOmniLight02','RTOmniLight03','RTOmniLight04','RTOmniLight05','RTOmniLight06','RTOmniLight07','RTOmniLight08','RTOmniLight09','RTOmniLight10','RTOmniLight11','RTOmniLight12','RTOmniLight13','RTOmniLight14','RTOmniLight15','RTOmniLight16','RTOmniLight17','RTOmniLight18','RTOmniLight19','RTOmniLight20','RTOmniLight21','RTOmniLight22','RTOmniLight23'),
        #Bright light for use in city
        'light' : ('RTOmniWeldLight',),
        #From HuruProjectWIKI
        #   Dock ropes and poles:
        'dockropes' : ('DockRope','DockRope01','DockRope02','DockRope03','DockRope04', 'DockRope05','DockRope06','DockRope07','DockRope08','DockRope09','DockRope10','DockRope11','DockRope12','DockRope13','DockRope14','DockRope15','DockRope16','DockRope17','DockRope18', 'DockRope19','DockRope20','DockRope21','DockRope22','DockRope23','DockRope24','DockRope25', 'DockRope26','DockRope27','DockRope28','DockRope29','DockRope30','DockRope31','DockRope32', 'DockRope33','FencePost17','FencePost21','FencePost22','FencePost23','FencePost24','FencePost25','FencePost26','FencePost27','FencePost28','FencePost29','FencePost30','FencePost31','FencePost32','FencePost33','FencePost34','FencePost35','FencePost36','FencePost37','FencePost38','FencePost39','FencePost40','FencePost41','FencePost42','FencePost43','FencePost44','FencePost45','FencePost46','FencePost47','FencePost48','FencePost49','FencePost50','FencePost51','FencePost52','FencePost53','FencePost54','FencePost55','FencePost56','FencePost57'),
        #   WORKLAMP AT THE DOCKS:
        'fworklamp' : ('WorkLampBattery02','WorkLampBlack02','WorkLampGlare24', 'WorkLampGlare25','WorkLightBars02'),
        #   BOXES AT TENT ON FIRST LANDING
        'fboxes' : ('WoodenBox14','WoodenBox15','WoodenBox16','WoodenBox17','WoodenBox18', 'WoodenBox19','WoodenBox20','WoodenBox21','WoodenBox22','WoodenBox23','WoodenBox24', 'WoodenBox25','WoodenBox26','WoodenBox27','WoodenBox28','WoodenBox29','WoodenBox30', 'WoodenBox31','WoodenBox32','WoodenBox33','WoodenBox34','WoodenBox35','WoodenBox36', 'WoodenBox37','WoodenBox38','WoodenBox39','WoodenBox40','WoodenBox41'),
        #   corner rubble
        'frubble' : ('RubGen01','RubGen02','RubGen03','RubPillar02','RubPillar05','RubPillar06','RubPillar07','Boulder03','Boulder05','Boulders02', 'FtpillarNEwTWO06','FtpillarNEwTWO07','FtpillarNEwTWO08','FtpillarNEwTWO09'),
        #   CLEAN UP TICKET OFFICE:
        'fticket' : ('FTreflectorBreak','FerryCAp','FTlensHouse','FTlensReflector'),
        #   SIGNPOST:
        'fsign' : ('ObeliskPlatform','FerryArrwHd','FerryArrwHdShadow','FerryIcon', 'GuildHallArrwHd','GuildHallArrwHdShadow','GuildHallIcon','PalaceArrwHd', 'PalaceArrwHdShadow','PalaceIcon','SignObelisk01','TinyLightFixture06','TinyLightFixture07'),
        #   FERRY CAVE GATE:
        'fgate' : ('Gate','GAteFrame'),
        #   POLES IN WATER AT PIER:
        'fpoles' : ('PierPost02','PierPost19','PierPost20','PierPost21','PierPost22', 'PierPost23','PierPost25','PierPost26','PierPost27','PierPostr24'),
        #   MIDDLE SECTION OF WALL:
        'fmosaic' : ('FTSmallMosaic01','FTSmallMosaic01Decal'),
        #   10 CHANGES:
        'fgame' : ('FTcanopy','DockRope','DockRope01','DockRope02','DockRope03','DockRope04', 'DockRope05','DockRope06','DockRope07','DockRope08','DockRope09','DockRope10','DockRope11', 'DockRope12','DockRope13','DockRope14','DockRope15','DockRope16','DockRope17','DockRope18','DockRope19','DockRope20','DockRope21','DockRope22','DockRope23','DockRope24','DockRope25', 'DockRope26','DockRope27','DockRope28','DockRope29','DockRope30','DockRope31','DockRope32', 'DockRope33','FencePost17','FencePost21','FencePost22','FencePost23','FencePost24','FencePost25','FencePost26','FencePost27','FencePost28','FencePost29','FencePost30', 'FencePost31','FencePost32','FencePost33','FencePost34','FencePost35','FencePost36','FencePost37','FencePost38','FencePost39','FencePost40','FencePost41','FencePost42', 'FencePost43','FencePost44','FencePost45','FencePost46','FencePost47','FencePost48','FencePost49','FencePost50','FencePost51','FencePost52','FencePost53','FencePost54', 'FencePost55','FencePost56','FencePost57','WorkLampBattery02','WorkLampBlack02','WorkLampGlare24','WorkLampGlare25','WorkLightBars02WoodenBox14','WoodenBox15','WoodenBox16','WoodenBox17','WoodenBox18','WoodenBox19','WoodenBox20','WoodenBox21','WoodenBox22', 'WoodenBox23','WoodenBox24','WoodenBox25','WoodenBox26','WoodenBox27','WoodenBox28','WoodenBox29','WoodenBox30','WoodenBox31','WoodenBox32','WoodenBox33','WoodenBox34', 'WoodenBox35','WoodenBox36','WoodenBox37','WoodenBox38','WoodenBox39','WoodenBox40','WoodenBox41RubGen01','RubGen02','RubGen03','RubPillar02','RubPillar05','RubPillar06', 'RubPillar07','Boulder03','Boulder05','Boulders02','FtpillarNEwTWO06','FtpillarNEwTWO07', 'FtpillarNEwTWO08','FtpillarNEwTWO09','FTreflectorBreak','FerryCAp','FTlensHouse','FTlensReflector','ObeliskPlatform','FerryArrwHd','FerryArrwHdShadow','FerryIcon','GuildHallArrwHd','GuildHallArrwHdShadow','GuildHallIcon','PalaceArrwHd','PalaceArrwHdShadow','PalaceIcon','SignObelisk01','TinyLightFixture06','TinyLightFixture07', 'Gate','GAteFrame','PierPost02','PierPost19','PierPost20','PierPost21','PierPost22', 'PierPost23','PierPost25','PierPost26','PierPost27','PierPostr24', 'FTSmallMosaic01','FTSmallMosaic01Decal'),
        #   CONES:
        'ferrycones' : ('OrangeCone','OrangeCone01','OrangeCone02','OrangeCone03','OrangeCone04', 'OrangeCone05','OrangeCone06','OrangeCone07','OrangeCone08','OrangeCone09','OrangeCone11', 'OrangeCone12','OrangeCone13','ph0-OrangeCone14','ph0-OrangeCone16'),
    },

    'Gira' : {
        'girabaskets' : ('basket01','basket02','basket03'),
        #The following gives a nice red light for gira at night
        'redgira' : ('RTLavaLight01','RTLavaLight02'),
        #GiraEnvironments by LCC
        #The following are different night time gira effects.
        'nightgira1' : ('Sun','RTDir-SunAmb01','RTDir-SunAmb02','RTDir-SunMain','RTDir-MoonMain','RTDir-MoonAmb01','VistaFake','Sky'),
        'nightgira2' : ('Sun','RTDir-SunAmb01','RTDir-SunAmb02','RTDir-MoonAmb01','VistaFake','Sky'),
        'nightgira3' : ('Sun','RTDir-SunMain','VistaFake'),
        'nightgira4' : ('RTDir-SunAmb01','RTDir-SunAmb02','RTDir-SunMain','RTDir-MoonAmb01','Sky'),
        'nightgira5' : ('RTDir-MoonMain','RTDir-SunMain','Sky'),
        'nightgira6' : ('RTDir-MoonMain','RTDir-MoonAmb01','RTDir-SunMain','RTDir-SunAmb01','RTDir-SunAmb02'),
        'nightgira7' : ('Sun','RTDir-SunMain','RTDir-MoonMain','Sky','VistaFake'),
        #The following is used to add or remove the lava.
        'lavagira' : ('LavaRiver','LavaSmokeEmit01','LavaSmokeEmit03','LavaSpatterEmit02','RTLavaLight02','RTLavaLight01','LavaRiverEdge','LavaSmokeEmit02','LavaSpatterEmit01'),
        #The following removes the water, waterfalls and fish.
        'watergira' : ('Fish01_Body01','Fish01_BoneLinker','Fish01_BoneLWing','Fish01_BoneRWing','Fish01_BoneTail','Fish01_LWing01','Fish01_RWing01','Fish01Master','Fish02_Body01','Fish02_BoneLinker', 'Fish02_BoneLWing','Fish02_BoneRWing','Fish02_BoneTail','Fish02_LWing01','Fish02_RWing01','Fish02Master','Fish03_Body01','Fish03_BoneLinker','Fish03_BoneLWing','Fish03_BoneRWing','Fish03_BoneTail','Fish03_LWing01','Fish03_RWing01','Fish03Master','Fish04_Body01','Fish04_BoneLinker','Fish04_BoneLWing','Fish04_BoneRWing','Fish04_BoneTail','Fish04_LWing01','Fish04_RWing01','Fish04Master','RTWaterFallLight01','RTWaterFallLight02','WaterBoneRipples01','WaterChurn01','WaterChurn02','WaterChurn03','WaterChurnSeam01','WaterChurnSeam02','WaterFall01','WaterFall02','WaterFall03','WaterFall04','WaterFall05','WaterFall06','WaterFallDropletKiller','WaterFallDropletsEmit','WaterFallMistEmit','WaterNoBugsBox01','waterNoBugsBox2','WaterNoBugsBox03','WaterReflDummy01','WaterReflDummy02','WaterReflDummy03','WaterRiver01','WaterRiver02','WaterShore01','WaterShore02','WaterShore03','WaterShoreFake01','WaterShoreFake02','WaterSurface01','WaterSurface02','WaterSurface03','WaterSurfaceFake01','WaterSurfaceFake02','WaterSurfaceFake03'),
        #The following is stuff to warp way out in space somewhere, it gets rid of bug
        #removers, excess sounds etc.
        'junkgira' : ('antiBugFumerolSmall01','antiBugFumerolSmall03','antiBugFumerolSmall05','antiBugFumerolSmall07','fumerolAntiBugRgn01','fumerolAntiBugRgn03','antiBugFumerolSmall02','antiBugFumerolSmall04','antiBugFumerolSmall06','antiBugFumerolSmall08','fumerolAntiBugRgn02','fumerolAntiBugRgn04','fumerolAntiBugRgn05','fumerolAntiBugRgn06','fumerolAntiBugRgn07','SfxBasket-SplashEmit01','SfxBasket-SplashEmit02','SfxBasket-SplashEmit03','SfxBasket-WaterEmit01','SfxBasket-WaterEmit02','SfxBasket-WaterEmit03','WaterNoBugsBox01','WaterNoBugsBox03','SfxLavaAmbEmit01L','SfxSoReg-Lava-Occlu01','SfxSoReg-Lava-Occlu03','SfxSoReg-Lava-Vol01','SfxSoReg-Lava-Vol03','SfxSoReg-Lava-Vol05','SfxSoReg-Lava-Vol07','SfxLavaAmbEmit01R','SfxSoReg-Lava-Occlu02','SfxSoReg-Lava-Occlu04','SfxSoReg-Lava-Vol02','SfxSoReg-Lava-Vol04','SfxSoReg-Lava-Vol06','SfxSoReg-Waterfall-Occlu01','SfxSoReg-Waterfall-Occlu02','SfxSoReg-Waterfall-Vol01','SfxSoReg-Waterfall-Vol02','SfxSoReg-Waterfall-Vol03','SfxSoReg-Waterfall-Vol04','SfxSoReg-Waterfall-Vol05','SfxSoReg-Waterfall-Vol06','SfxSoReg-Waterfall-Vol07','SfxSoReg-Waterfall-Vol08','SfxSoReg-Waterfall-Vol09','SfxSoReg-Waterfall-Vol10','SfxSoReg-Waterfall-Vol11','SfxStereizerDummy','SfxWaterfallEmit01L','SfxWaterfallEmit01R','SfxWaterfallEmit02L','SfxWaterfallEmit02R','SfxWaterfallEmit06L','SfxWaterfallEmit06R','SfxWaterfallEmit07L','SfxWaterfallEmit07R','SfxWaterfallEmit08'),
        'GiraSafe' : ('PanicLinkReg01','PanicLinkReg02','PanicLinkReg03'),
    },

    'Neighborhood' : {
        'hoodcones' : ('OrangeCone01','OrangeCone04','OrangeCone05','OrangeCone11','OrangeCone12','OrangeCone15','OrangeCone16','OrangeCone17'),
        'hoodfire' : ('MarblePhy06','MarblePhy07','MarblePhy08'),
        #Color Hood Lights by LiquorCooChee
        #where ever you move the lights, when the buttons on the
        #bridge are operated, it turns them on/off in their new location
        'orangehood' : ('grdnRTOmniOrange01','grdnRTOmniOrange02','grdnRTOmniOrange03'),
        'greenhood' : ('grdnRTOmniGreen01','grdnRTOmniGreen03','grdnRTOmniGreen05','grdnRTOmniGreen02','grdnRTOmniGreen04'),
        'bluehood' : ('grdnRTOmniBlue01','grdnRTOmniBlue03','grdnRTOmniBlue05','grdnRTOmniBlue07','grdnRTOmniBlue09','grdnRTOmniBlue11','grdnRTOmniBlue02','grdnRTOmniBlue04','grdnRTOmniBlue06','grdnRTOmniBlue08','grdnRTOmniBlue10'),
        #sparks work anywhere in hood, of course the sparklers need to be active for
        #this to be of use
        'sparks' : ('SparklerEmit01','SparklerEmit02','SparklerEmit03','SparklerEmit04','SprayEmit'),
        #mlight only works in private rooms
        'mlight' : ('MarbleLight01','MarbleLight02','MarbleLight03','MarbleLight04','MarbleLight05'),
        #For some reason, turning off the physics/collision won't remove the collision
        #from the fountain
        'hoodfount' : ('FountainLightFixture01','FountainLightFixture02','FountainLightFixture03','FountainLightFixture04','FountainRipple','FountainRipple02','FountainSpotBillboard01','FountainSpotBillboard02','FountainSpotBillboard03','FountainSpotBillboard04','FountPillar01','FountPillar02','FountPillar03','FountPillar04','FountainWaterBase','Fountian'),
    },

    'Personal' : {
        'reltologs' : ('StLog23','StLog24','StLog25','StLog26','StLog27','StLog28'),
        'reltostones' : ('KickBoulder','KickBoulder01','KickBoulder02'),
        #By Greypiffle
        'reltotrees' : ('PonderosaBig_02','PonderosaBig_03','PonderosaBig_04','PonderosaBig_05','PondorosaBig_06','PondorosaBig_07','PondorosaBig_08','PondorosaBig_09','PondorosaBig_10'),
        'othertrees' : ('Ponderosa17','Ponderosa18','Ponderosa19','Ponderosa20','Ponderosa21','Ponderosa22','Ponderosa24','Ponderosa25','Ponderosa26','Ponderosa27','Ponderosa28','Ponderosa32','Ponderosa33','Ponderosa34','Ponderosa35','Ponderosa36','Ponderosa39','Ponderosa40','Ponderosa41','Ponderosa42'),
        'dock' : ('DockNew01','DockPost64','DockPost68','DockPost70','DockPost72','DockPost74','DockPost75','DockPost76','DockPost77','DockPost78','DockPost79','DockPost80','DockPost81','DockRope02','DockRope03','DockRope04','DockRope05','DockRope06','DockRope07'),
        #The Library's many objects
        'left_shelf' : ('ShelfA','ShelfAbkLOCK01','ShelfAbkLOCK02','ShelfAbkLOCK03','ShelfAbkLOCK04','ShelfAbkLOCK05','ShelfAbkLOCK06','ShelfAbkLOCK07','ShelfAbkLOCK08','ShelfAbkLOCK09','ShelfAbkLOCK10','ShelfAbkLOCK11','ShelfAbkLOCK12','ShelfAbkLOCK13','ShelfAbkLOCK14','ShelfAbkLOCK15','ShelfAbkLOCK16','ShelfAbkLOCK17','ShelfAbkLOCK18','ShelfAbkLOCK19','ShelfAbkLOCK20','ShelfAbkLOCK21','ShelfAbkLOCK22','ShelfAbkLOCK23','ShelfAbkLOCK24','ShelfAbkLOCK25','ShelfAbkLOCK26','ShelfAbkLOCK27','ShelfAbkLOCK28','ShelfAbkLOCK29','ShelfAbkLOCK30','ShelfAbkLOCK31','ShelfAbkLOCK32','ShelfAbkLOCK33','ShelfAbkLOCK34','ShelfAbkLOCK35','ShelfAbkLOCK36','ShelfAbkTRAY01','ShelfAbkTRAY02','ShelfAbkTRAY03','ShelfAbkTRAY04','ShelfAbkTRAY05','ShelfAbkTRAY06','ShelfAbkTRAY07','ShelfAbkTRAY08','ShelfAbkTRAY09','ShelfAbkTRAY10','ShelfAbkTRAY11','ShelfAbkTRAY12','ShelfAbkTRAY13','ShelfAbkTRAY14','ShelfAbkTRAY15','ShelfAbkTRAY16','ShelfAbkTRAY17','ShelfAbkTRAY18','ShelfAbkTRAY19','ShelfAbkTRAY20','ShelfAbkTRAY21','ShelfAbkTRAY22','ShelfAbkTRAY23','ShelfAbkTRAY24','ShelfAbkTRAY25','ShelfAbkTRAY26','ShelfAbkTRAY27','ShelfAbkTRAY28','ShelfAbkTRAY29','ShelfAbkTRAY30','ShelfAbkTRAY31','ShelfAbkTRAY32','ShelfAbkTRAY33','ShelfAbkTRAY34','ShelfAbkTRAY35','ShelfAbkTRAY36','ShelfATrayCLK01','ShelfATrayCLK02','ShelfATrayCLK03','ShelfATrayCLK04','ShelfATrayCLK05','ShelfATrayCLK06','ShelfATrayCLK07','ShelfATrayCLK08','ShelfATrayCLK09','ShelfATrayCLK10','ShelfATrayCLK11','ShelfATrayCLK12','ShelfATrayCLK13','ShelfATrayCLK14','ShelfATrayCLK15','ShelfATrayCLK16','ShelfATrayCLK17','ShelfATrayCLK18','ShelfATrayCLK19','ShelfATrayCLK20','ShelfATrayCLK21','ShelfATrayCLK22','ShelfATrayCLK23','ShelfATrayCLK24','ShelfATrayCLK25','ShelfATrayCLK26','ShelfATrayCLK27','ShelfATrayCLK28','ShelfATrayCLK29','ShelfATrayCLK30','ShelfATrayCLK31','ShelfATrayCLK32','ShelfATrayCLK33','ShelfATrayCLK34','ShelfATrayCLK35','ShelfATrayCLK36'),
        'right_shelf' : ('ShelfB','YeeshaJournal'),
        'normalbooks' : ('ShelfA_book01','ShelfA_book02','ShelfA_book03','ShelfA_book04','ShelfA_book05','ShelfA_book06','ShelfA_book07','ShelfA_book08','ShelfA_book09'),
        'extrabooks' : ('ShelfA_Book007',
                        'ShelfA_Book008','ShelfA_Book009','ShelfA_Book010',
                        'ShelfA_Book011','ShelfA_Book012','ShelfA_Book013',
                        'ShelfA_Book014','ShelfA_Book015','ShelfA_Book016',
                        'ShelfA_Book017','ShelfA_Book018','ShelfA_Book019',
                        'ShelfA_Book020','ShelfA_Book021','ShelfA_Book022',
                        'ShelfA_Book023','ShelfA_Book024','ShelfA_Book025',
                        'ShelfA_Book026','ShelfA_Book027','ShelfA_Book028'),
        'extrabooks2' : ('ShelfA_book15',
                         'ShelfA_book16','ShelfA_book17','ShelfA_book18',
                         'ShelfA_book19','ShelfA_book20','ShelfA_book21',
                         'ShelfA_book22','ShelfA_book23','ShelfA_book24',
                         'ShelfA_book25','ShelfA_book26','ShelfA_book27',
                         'ShelfA_book28','ShelfA_book29','ShelfA_book30',
                         'ShelfA_book31','ShelfA_book32','ShelfA_book33',
                         'ShelfA_book34','ShelfA_book35','ShelfA_book36'),
        #Use /drawoff on this and then /drawon ImgrPhotoPlane02 to make a cool floating image screen :)
        'psnlimager' : ('ImagerBody02','ImagerBracket03','ImagerBracket04','ImagerPost00','ImagerPost01','ImagerPostBase','ImagerPostBase01','ImgrHinge05','ImgrHinge06','ImgrHinge07','ImgrHinge08','Imgr-KI-Glow02','Imgr-KI-Logo02','ImgrStaticPlane02','ImgrPhotoPlane02','Rope','Rope01','Rope02','Rope03'),
        'PersonalSafe' : ('PanicLinkRegion',),
        'marbles' : ('MarblePhy06','MarblePhy07','MarblePhy08','MarblePhy09',
                     'MarblePhy10'),
    },

    'Kadish' : {
        #The following can be a lot of fun to play with while you are visiting Kadish.
        #It might be a good idea not to enable the physics on this set of objects :)
        #rleaf1 and rleaf2 only work in telescope area of kadish
        'rleaf1' : ('RedLeaf00','RedLeaf00b','RedLeaf01','RedLeaf01b','RedLeaf02','RedLeaf02b','RedLeaf03','RedLeaf03b','RedLeaf04','RedLeaf04b','RedLeaf05','RedLeaf05b','RedLeaf06','RedLeaf06b','RedLeaf07','RedLeaf07b','RedLeaf08','RedLeaf08b','RedLeaf09','RedLeaf09b','RedLeaf10','RedLeaf100','RedLeaf101','RedLeaf102','RedLeaf103','RedLeaf104','RedLeaf105','RedLeaf106','RedLeaf107','RedLeaf108','RedLeaf109','RedLeaf10b','RedLeaf11','RedLeaf110','RedLeaf111','RedLeaf112','RedLeaf113','RedLeaf114','RedLeaf115','RedLeaf116','RedLeaf117','RedLeaf11b','RedLeaf12','RedLeaf13','RedLeaf14','RedLeaf15','RedLeaf16','RedLeaf17','RedLeaf18','RedLeaf19','RedLeaf20','RedLeaf21','RedLeaf21b','RedLeaf22','RedLeaf23','RedLeaf24','RedLeaf24b','RedLeaf25','RedLeaf25b','RedLeaf26','RedLeaf26b','RedLeaf27','RedLeaf27b','RedLeaf28','RedLeaf28b','RedLeaf29','RedLeaf29b','RedLeaf30','RedLeaf31','RedLeaf32','RedLeaf33','RedLeaf34','RedLeaf35','RedLeaf36','RedLeaf37','RedLeaf38','RedLeaf39','RedLeaf40','RedLeaf41','RedLeaf42','RedLeaf43','RedLeaf44','RedLeaf45','RedLeaf46','RedLeaf47','RedLeaf48','RedLeaf49','RedLeaf50','RedLeaf51','RedLeaf52','RedLeaf53','RedLeaf54','RedLeaf55','RedLeaf56','RedLeaf57','RedLeaf58','RedLeaf59','RedLeaf60','RedLeaf61','RedLeaf62','RedLeaf63','RedLeaf64','RedLeaf65','RedLeaf66','RedLeaf67','RedLeaf68','RedLeaf69','RedLeaf70','RedLeaf71','RedLeaf72','RedLeaf73','RedLeaf74','RedLeaf75','RedLeaf76','RedLeaf77','RedLeaf78','RedLeaf79','RedLeaf80','RedLeaf81','RedLeaf82','RedLeaf83','RedLeaf84','RedLeaf85','RedLeaf86','RedLeaf87','RedLeaf88','RedLeaf89','RedLeaf90','RedLeaf91','RedLeaf92','RedLeaf93','RedLeaf94','RedLeaf95','RedLeaf96','RedLeaf97','RedLeaf98','RedLeaf99'),
        'rleaf2' : ('RedLeaf41','RedLeaf42','RedLeaf43','RedLeaf44','RedLeaf45','RedLeaf46','RedLeaf47','RedLeaf48','RedLeaf49','RedLeaf50','RedLeaf51','RedLeaf52','RedLeaf53','RedLeaf54','RedLeaf55','RedLeaf56','RedLeaf57','RedLeaf58','RedLeaf59','RedLeaf60','RedLeaf61','RedLeaf62','RedLeaf63','RedLeaf64','RedLeaf65','RedLeaf66','RedLeaf67','RedLeaf68','RedLeaf69','RedLeaf70','RedLeaf71','RedLeaf72','RedLeaf73'),
        'KadishSafe' : ('PanicLink','PitPanicLink','PanicLinkRegion','rgnPanicLink','PanicRegionGlwRM','VistaPanicLink'),
    },

    'Teledahn' : {
        #The following object groups are from the slave cave in Teledahn
        #tstones and tbones only work near the slave cave in teledahn
        'tstones' : ('RollingRock01','RollingRock02','RollingRock03','RollingRock04','RollingRock05','RollingRock06','RollingRock07','RollingRock08','RollingRock09','RollingRock10'),
        'tbones' : ('Skull01','Skull02','Bone-C-17','Bone-C-18','Bone-Q-12'),
        'trocks' : ('FinalRock01','FinalRock02','FinalRock03','FinalRock04','FinalRock05','FinalRock06','FinalRock07','FinalRock08','FinalRock09','FinalRock10','FinalRock11','FinalRock12','FinalRock13','FinalRock14','FinalRock15','FinalRock16','FinalRock17','FinalRock18','FinalRock19','FinalRock20','FinalRock21','FinalRock22'),
        #By D'Lanor
        #If you use /objhere shroomspawn all of Shroomies spawn points will be moved
        #to just above your avatar position. Great for closeups!
        'shroomspawn' : ('SpawnPtFar01','SpawnPtFar02','SpawnPtFar03','SpawnPtFar04','SpawnPtFar05','SpawnPtMid01','SpawnPtMid02','SpawnPtMid03','SpawnPtMid04','SpawnPtMid05','SpawnPtNear01','SpawnPtNear02','SpawnPtNear03','SpawnPtNear04','SpawnPtNear05'),
    },

    'Cleft' : {
        #CleftEnvironments by LCC
        'nightcleft' : ('DesertPlane','DesertPlane1','DesertPlane2','DesertPlane3','DesertPlane4','farOffMountainRange','MountainRangeSplit','MountainRangeSplit2','TheVolcano','skyDome','SunGlow'),
        #Kickable pieces of wood in the Cleft
        'cleftwood' : ('kitLog05','kitLog15','kitLog18','kitLog21','PhysBoard02'),
    },

    'GreatZero' : {
        #GZ Lightning Flashes
        'gzlight' : ('RT-ArcLight01','RT-ArcLight02','RT-ArcLight03','RT-ArcLight04','RT-ArcLight05'),
    },

    'Garrison' : {
        'GarrisonSafe' : ('PanicLinkBox','PanicLinkYeeshaPage','PanicLinkYeeshaPage01','PanicLinkYeeshaPage02','PanicLinkWellSubregion','pillar-well-jump-panic'),
    },

    'Garden' : {
        #  The fountain streams
        'streams' : ('Tier0Party00','Tier0Party01','Tier0Party02','Tier0Party03','Tier0Party04','Tier0Party05','Tier1Party00','Tier1Party01','Tier1Party02','Tier1Party03','Tier1Party04','Tier1Party05','Tier2Party00','Tier2Party01','Tier2Party02','Tier2Party03','Tier2Party04','Tier2Party05'),
        #  use /drawoff and /drawon to stop and start flat trees from swaying in the
        #breeze
        'sway1' : ('TreeBone','TreeBone01','TreeBone02','TreeBone03','TreeBone04','TreeBone05','TreeBone06','TreeBone07','TreeBone08','TreeBone09','TreeBone10','TreeBone11','TreeBone12','TreeBone13','TreeBone14','TreeBone15','TreeBone16','TreeBone17','TreeBone18'),
        #  use /drawoff and /drawon to stop and start brain trees from swaying in the
        #breeze
        'sway2' : ('TroomBone','TroomBone01','TroomBone02','TroomBone03','TroomBone04','TroomBone05','TroomBone06','TroomBone07','TroomBone08','TroomBone09','TroomBone10','TroomBone11','TroomBone12','TroomBone13','TroomBone14','TroomBone15','TroomBone16','TroomBone17','TroomBone18','TroomBone19','TroomBone20','TroomBone21','TroomBone22','TroomBone23','TroomBone24','TroomBone25'),
        #  use /drawoff and /drawon to stop and start puffer pods from puffing
        'puffbone' : ('PufferBone00','PufferBone01','PufferBone02','PufferBone03','PufferBone05','PufferBone06','PufferBone07','PufferBone08','PufferBone09','PufferBone10','PufferBone11','PufferBone12','PufferBone13','PufferBone14','PufferBone16','PufferBone17','PufferBone18','PufferBone19','PufferBone20','PufferBone21'),
        #  The following are the spores that are shot out of puffer pods
        'puffball' : ('PuffterBall00','PuffterBall01','PuffterBall02','PuffterBall03','PuffterBall05','PuffterBall06','PuffterBall07','PuffterBall08','PuffterBall09','PuffterBall10','PuffterBall11','PuffterBall12','PuffterBall13','PuffterBall14','PuffterBall16','PuffterBall17','PuffterBall18','PuffterBall19','PuffterBall20','PuffterBall21'),
    },

    'Personal02' : {
        'Personal02Safe' : ('PanicLinkRegion',),
    },

    'AhnySphere02' : {
        'AhnySphere02Safe' : ('PanicLinkRegion',),
    },

    'AhnySphere03' : {
        'AhnySphere03Safe' : ('PanicLinkRegion',),
    },

    'AhnySphere04' : {
        'AhnySphere04Safe' : ('PanicLinkBox',),
    },

    'Descent' : {
        'DescentSafe' : ('Panic region Linkout',),
    },
}
# end of ObjectLists

# begin of StructLists
StructLists = {
    'Personal' : {
        # The /treeson command converted to structure list
        'trees' : ([['PonderosaBig_02'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[45.304691,32.544270,5.200000]],
                [['PonderosaBig_03'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[68.070564,37.050888,48.490932]],
                [['PonderosaBig_04'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-61.327957,-8.160940,-3.081162]],
                [['PonderosaBig_05'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[13.743594,6.063022,0.000000]],
                [['PondorosaBig_06'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-6.779923,3.801187,0.044419]],
                [['PondorosaBig_07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[4.908178,9.684015,0.463208]],
                [['PondorosaBig_08'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-1.247162,15.384789,1.570511]],
                [['PondorosaBig_09'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[10.143805,-4.795108,-1.793024]],
                [['PondorosaBig_10'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[0.000000,0.000000,0.000000]]),
        #Pile logs on right side of hut stairs for cleaning up your Relto
        'logpile' : ([['StLog23'],[-0.963622,0.264011,-0.041606],[-0.031769,0.041424,0.998636],[45.057846,-2.799302,13.501013]],
                [['StLog24'],[-0.704897,-0.669629,-0.233917],[0.151515,0.180020,-0.971924],[44.420967,-4.119459,14.151592]],
                [['StLog25'],[-0.957430,-0.164092,0.237490],[0.286966,-0.451900,0.844652],[44.497066,-3.582477,13.518958]],
                [['StLog26'],[0.699664,-0.607127,-0.376651],[0.095390,-0.443076,0.891395],[45.848625,-4.149622,13.559573]],
                [['StLog27'],[-0.737751,-0.653885,0.167800],[0.360062,-0.591401,-0.721526],[44.918621,-5.112301,13.689071]],
                [['StLog28'],[0.724164,0.369438,0.582325],[-0.091431,0.888383,-0.449906],[44.100719,-3.169155,14.052407]]),
        #Pile rocks on left side of hut stairs for cleaning up your relto
        'rockpile' : ([['KickBoulder'],[0.190695,-0.891589,0.410736],[0.347998,-0.329841,-0.877555],[33.796043,9.012926,13.783654]],
                [['KickBoulder01'],[0.446045,-0.706502,0.549454],[-0.219041,-0.681410,-0.698356],[32.887398,10.041360,13.607865]],
                [['KickBoulder02'],[0.552258,-0.614692,0.563174],[-0.112311,-0.724232,-0.680349],[33.342323,10.974363,13.400828]]),
        # big logs above the far relto island
        'biglog' : ([['StLog23'],[-3.529411,1.882353,0.000000],[0.000000,0.000000,4.000000],[-70.503059,112.103516,4.561522],[4.000000,4.000000,4.000000]],
                [['StLog24'],[-3.529411,1.882353,0.000000],[0.000000,0.000000,4.000000],[-70.503059,112.103546,6.561520],[4.000000,4.000000,4.000000]],
                [['StLog25'],[-3.529411,1.882353,0.000000],[0.000000,0.000000,4.000000],[-70.503059,112.103546,8.561522],[4.000000,4.000000,4.000000]],
                [['StLog26'],[-3.529411,1.882353,0.000000],[0.000000,0.000000,4.000000],[-70.503075,112.103531,10.561520],[4.000000,4.000000,4.000000]],
                [['StLog27'],[-3.529411,1.882353,0.000000],[0.000000,0.000000,4.000000],[-70.503059,112.103546,12.561520],[4.000000,4.000000,4.000000]],
                [['StLog28'],[-3.529411,1.882353,0.000000],[0.000000,0.000000,4.000000],[-70.503059,112.103546,14.561516],[4.000000,4.000000,4.000000]]),
        # Be sure to /drawon fissurestarfield before using the reltostars
        # For a much nicer effect, /drawoff skyhigh and change /setlinear to 0 0 0
        'reltostars' : ([['fissurestarfield'],[0.000001,8.000000,-0.000001],[-0.000000,-0.000001,-8.000000],[0.000000,0.000000,20.000000],[8,8,8]],),
        # This with other features enabled will give you a Great new look for your relto,
        # You want to drawoff /drawoff SkyHigh SkyLow
        # Then you want to use /setlinear 0 0 0
        # Then set fogcolor to /fogcolor .0 .0 5
        # Finally use the /struct reltostars2
        # to set up the stary sky,
        # NOTE: This is well worth it, IMO
        'reltostars2' : ([['FissureStarField'],[0.000000,20.000000,-0.000002],[0.000000,-0.000002,-20.000000],[0.000000,0.000000,-20.000000],[20,20,20]],),
        'noreltostars' : ([['fissurestarfield'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[0.000000,0.000000,0.000000],[1,1,1]],),
        # You will need your Islands Yeesha page and you will also need to nab your
        # Bahro poles back. But that's OK, the Bahro don't need them anymore :)
        'bahrohuts' : ([['YeeshaPoleBookPedestal-grsn'],[-2.589628,1.514539,0.000000],[0.000000,0.000000,3.000000],[-29.186209,70.078171,7.992509],[3,3,3]],
                [['YeeshaPoleBookPedestal-grdn'],[0.766620,2.900395,0.000000],[0.000000,0.000000,3.000000],[-33.032978,51.714569,7.574988],[3,3,3]],
                [['YeeshaPoleBookPedestal-kdsh'],[-1.168255,-2.763183,0.000000],[0.000000,0.000000,3.000000],[2.904434,60.880287,7.419312],[3,3,3]],
                [['YeeshaPoleBookPedestal-tldn'],[0.000000,-3.000000,0.000000],[0.000000,0.000000,3.000000],[20.753391,68.617363,4.626731],[3,3,3]]),
    },

    'city' : {
        # bowlpins - sets up a 10 pin bowling game at the upper landing section of the great stairs
        # a good way is to get on center lane and rotate urself at /y 85 and aim for center
        'bowlpins' : ([['orangecone01'],[-0.389418,-0.921061,0.000000],[0.000000,0.000000,1.000000],[-6.430493,-302.551941,146.152176]],
                [['orangecone02'],[-0.389418,-0.921061,0.000000],[0.000000,0.000000,1.000000],[-3.100331,-302.622894,146.152176]],
                [['orangecone03'],[-0.389418,-0.921061,0.000000],[0.000000,0.000000,1.000000],[0.015439,-302.551758,146.152176]],
                [['orangecone04'],[-0.942784,0.333394,-0.002681],[0.000000,0.000000,1.000000],[3.128611,-301.845581,146.115387]],
                [['orangecone05'],[-0.389418,-0.921061,0.000000],[0.000000,0.000000,1.000000],[-4.758247,-299.667908,146.144577]],
                [['orangecone12'],[0.564642,-0.825336,0.000000],[0.000000,0.000000,1.000000],[-1.598775,-298.966034,146.151871]],
                [['orangecone07'],[-0.389418,-0.921061,0.000000],[0.000000,0.000000,1.000000],[1.950155,-299.579071,146.150208]],
                [['orangecone08'],[-0.388236,-0.919238,-0.065379],[0.000000,0.000000,1.000000],[-2.941409,-296.631531,146.416458]],
                [['orangecone09'],[-0.389418,-0.921061,0.000000],[0.000000,0.000000,1.000000],[0.595483,-296.385468,146.156052]],
                [['orangecone10'],[-0.909297,0.416148,0.000000],[0.000000,0.000000,1.000000],[-1.390046,-292.898651,146.152008]]),
        #ConeHenge - created by request for Kierra_Windsong and Greypiffle on Tapestry Shard.
        'conehenge' : ([['ALYOrangeCone12'],[-0.838671,0.544639,-0.000000],[0.000000,0.000000,1.000000],[107.600616,-149.025574,216.297729]],
                [['ALYOrangeCone11'],[-0.998630,0.052336,-0.000000],[0.000000,0.000000,1.000000],[111.763214,-147.583282,216.308990]],
                [['ALYOrangeCone10'],[-0.173648,-0.984808,-0.000000],[-0.000000,0.000000,1.000000],[115.838974,-148.098953,216.307770]],
                [['OrangeCone11b'],[-0.927184,0.374607,-0.000000],[0.000000,0.000000,1.000000],[120.209511,-149.094345,216.300583]],
                [['OrangeCone06b'],[-0.999391,-0.034899,-0.000000],[0.000000,0.000000,1.000000],[123.516808,-151.815659,216.304367]],
                [['OrangeCone19'],[-0.996195,-0.087156,-0.000000],[-0.000000,0.000000,1.000000],[125.316269,-156.613358,216.304962]],
                [['OrangeCone18'],[0.104529,-0.994522,-0.000000],[0.000000,0.000000,1.000000],[126.063583,-161.692444,216.308655]],
                [['OrangeCone12'],[-1.000000,-0.000000,-0.000000],[-0.000000,0.000000,1.000000],[124.652817,-165.750656,216.302338]],
                [['OrangeCone10'],[0.258819,-0.965926,-0.000000],[0.000000,0.000000,1.000000],[121.027451,-169.761230,216.303864]],
                [['OrangeCone09'],[-0.173648,-0.984808,-0.000000],[-0.000000,0.000000,1.000000],[116.636932,-171.568680,216.300629]],
                [['OrangeCone08'],[0.518212,0.660321,0.543536],[0.854879,-0.381149,-0.352006],[111.843849,-170.985260,216.295181]],
                [['OrangeCone05'],[-0.587785,0.809017,-0.000000],[0.000000,0.000000,1.000000],[107.732079,-169.330261,216.298965]],
                [['OrangeCone04'],[-0.213987,-0.960290,0.179033],[-0.926681,0.141588,-0.348159],[104.879921,-167.415314,216.293716]],
                [['OrangeCone03'],[0.087156,0.996195,-0.000000],[0.000000,0.000000,1.000000],[102.954956,-162.775864,216.309418]],
                [['OrangeCone01'],[0.469472,0.882948,-0.000000],[0.000000,0.000000,1.000000],[102.405106,-157.952698,216.303970]],
                [['OrangeCone'],[0.258819,0.965926,-0.000000],[0.000000,0.000000,1.000000],[114.503761,-159.615219,216.308807]]),
        #For telescope on the Dakotah Rooftop
        #Use this then use the scope
        # CAM TO SELF
        'telecam1' : ([['TelescopeCamera'],[-0.976541,-0.215332,0.000000],[0.215332,-0.976541,-0.000000],[-49.339653,-156.692108,280.398407]],
                [['TelescopeCamera.Target'],[-0.544639,-0.838671,0.000000],[0.000000,0.000000,1.000000],[-42.781189,-144.524445,280.370789]]),
        # Cam to Spyroom
        'telecam2' : ([['TelescopeCamera'],[-0.976541,-0.215332,0.000000],[0.215332,-0.976541,-0.000000],[-124.239822,-125.579056,261.671143]],
                [['TelescopeCamera.target'],[-0.544639,-0.838671,0.000000],[0.000000,0.000000,1.000000],[-152.849991,-143.949203,261.671143]]),
        # Cam to library
        'telecam3' : ([['TelescopeCamera'],[-0.976541,-0.215332,0.000000],[0.215332,-0.976541,0.000000],[749.213684,-540.252808,331.400360]],
                [['TelescopeCamera.target'],[-0.544639,-0.838671,0.000000],[0.000000,0.000000,1.000000],[838.647095,-644.285889,275.988098]]),
        # Closeup cam of guildhall smoke/explosion
        'telecam4' : ([['TelescopeCamera'],[-0.976541,-0.215332,0.000000],[0.215332,-0.976541,0.000000],[8.136490,-3.413898,507.673737]],
                [['TelescopeCamera.target'],[-0.544639,-0.838671,0.000000],[0.000000,0.000000,1.000000],[-11.863510,226.586105,477.673737]]),
        'conestar' : ([['OrangeCone01'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-62.775257,-13.453857,267.470856]],
                [['OrangeCone02'],[0.000000,-1.000000,0.000000],[-0.000000,0.000000,-1.000000],[-62.575256,-13.453857,270.170837]],
                [['OrangeCone03'],[0.000000,-1.000000,0.000000],[0.766044,0.000000,0.642788],[-63.675259,-13.453857,267.870880]],
                [['OrangeCone04'],[0.000000,-1.000000,0.000000],[-0.642787,0.000000,0.766045],[-61.775257,-13.453857,267.570831]],
                [['OrangeCone05'],[0.000000,-1.000000,0.000000],[0.766044,0.000000,-0.642788],[-63.475258,-13.453857,269.970825]],
                [['OrangeCone06'],[0.000000,-1.000000,-0.000000],[-0.342020,-0.000000,0.939693],[-61.775257,-12.953856,270.170837]],
                [['OrangeCone06b'],[0.000000,0.000000,1.000000],[0.000000,1.000000,-0.000000],[-62.775257,-13.953857,268.670837]],
                [['OrangeCone07'],[0.000000,-0.000000,-1.000000],[0.000000,-1.000000,0.000000],[-62.575256,-12.153858,268.470825]],
                [['OrangeCone07b'],[0.000000,-1.000000,0.000000],[1.000000,0.000000,-0.000000],[-63.670113,-13.278736,268.670837]],
                [['OrangeCone08'],[-0.669131,-0.743145,0.000000],[0.000000,0.000000,1.000000],[-63.275257,-13.453857,273.170837]],
                [['OrangeCone08b'],[-0.809017,-0.000000,-0.587785],[0.000000,1.000000,-0.000000],[-62.575256,-9.053857,268.470856]],
                [['OrangeCone09'],[-0.848048,-0.000000,-0.529919],[0.000000,-1.000000,0.000000],[-62.775257,-17.053858,268.670868]],
                [['OrangeCone09b'],[0.000000,-1.000000,0.000000],[-1.000000,0.000000,0.000000],[-61.075256,-13.453857,268.370850]],
                [['OrangeCone10'],[-0.000000,-0.998630,-0.052336],[-1.000000,0.000000,0.000000],[-66.675255,-13.253857,268.670837]],
                [['OrangeCone10b'],[0.000000,-0.544639,0.838671],[1.000000,-0.000000,-0.000000],[-57.975258,-12.903857,268.670837]],
                [['OrangeCone11b'],[0.173648,-0.984808,-0.000000],[-0.000000,0.000000,-1.000000],[-62.125256,-13.253857,264.420807]]),
        # Alternate cleancity structure that resets many of the objects used in other structures for the city usefull
        # for cleaning up between showing off (submitted by Gazerwolf)
        'cleancity' : ([['OrangeCone01'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[224.801544,-361.386505,181.002319]],
                [['OrangeCone02'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[219.518631,-370.206726,180.902100]],
                [['OrangeCone03'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[232.535660,-369.675049,180.878220]],
                [['OrangeCone04'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[229.341522,-347.563446,181.420746]],
                [['OrangeCone05'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[180.165131,-330.472626,180.767014]],
                [['OrangeCone06'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[169.231613,-329.470734,179.972794]],
                [['OrangeCone06b'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[484.616119,-332.166565,296.740173]],
                [['OrangeCone07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[155.093262,-317.643463,180.767014]],
                [['OrangeCone07b'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[480.295563,-333.791260,296.740173]],
                [['OrangeCone08'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[153.212341,-297.466003,180.767014]],
                [['OrangeCone08b'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[466.794281,-331.155975,296.740173]],
                [['OrangeCone09'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[230.250076,-339.584564,181.420746]],
                [['OrangeCone09b'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[462.588684,-331.860046,296.740173]],
                [['OrangeCone10'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[189.122055,-327.315918,180.767014]],
                [['OrangeCone10b'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[513.060913,-280.990936,296.915283]],
                [['OrangeCone11'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[239.092972,-364.321411,180.186584]],
                [['OrangeCone11b'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[498.518921,-270.391785,296.915283]],
                [['OrangeCone12'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[500.922607,-275.169037,296.915283]],
                [['OrangeCone18'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[31.097286,-68.706833,223.373749]],
                [['OrangeCone19'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[12.837772,-51.407848,221.777603]],
                [['ALYOrangeCone10'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-189.704971,-217.542770,200.020233]],
                [['ALYOrangeCone11'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-200.048630,-202.682877,199.942902]],
                [['ALYOrangeCone12'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-203.366226,-197.551559,199.942902]],
                [['ALYOrangeCone13'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-188.141663,-220.256851,198.665863]],
                [['drctentmaster'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[0.000000,0.000000,0.000000]],
                [['smokeemitter01'],[0.000000,-0.788011,-0.615662],[0.000000,-0.615662,0.788011],[21.393028,185.388245,478.887451]],
                [['smokeemitter02'],[-0.190051,-0.791621,-0.580703],[-0.135562,-0.564658,0.814115],[-23.564562,171.555710,478.887451]],
                [['archofkerath'],[0.000000,1.041852,0.000000],[0.000000,0.000000,1.177293],[-2.325882,-2022.840088,0.046170]],
                [['shroomiepict'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-104.589180,-85.958916,224.598236]],
                [['mapboard'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[0.000000,0.000000,0.000000]],
                [['kdshgallerydoor01'],[-0.629320,-0.777146,0.000000],[0.000000,0.000000,1.000000],[172.711304,-357.800293,184.895203]],
                [['RTOmniLight01'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[34.592800,-154.062576,227.817108]],
                [['RTOmniLight02'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[41.292091,-176.093765,213.708771]],
                [['RTOmniLight03'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[54.437218,-209.333893,213.708771]],
                [['RTOmniLight04'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[63.179092,-226.283539,199.918503]],
                [['RTOmniLight05'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[90.597733,-259.034546,199.918503]],
                [['RTOmniLight06'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[107.106041,-274.276917,185.499680]],
                [['RTOmniLight07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[237.948792,-457.354797,214.983536]],
                [['RTOmniLight08'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[244.429688,-471.847321,214.983536]],
                [['RTOmniLight09'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[230.890625,-497.615265,214.983536]],
                [['RTOmniLight10'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[215.481705,-497.020142,214.983536]],
                [['RTOmniLight11'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[263.574585,-526.745239,244.182678]],
                [['RTOmniLight12'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[365.720581,-550.259521,244.182678]],
                [['RTOmniLight13'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[407.948914,-517.945068,281.798462]],
                [['RTOmniLight14'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[423.786865,-519.379944,281.798462]],
                [['RTOmniLight15'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[413.502716,-482.830872,290.646790]],
                [['RTOmniLight16'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[397.462341,-486.340271,290.646790]],
                [['RTOmniLight17'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[393.692780,-456.491821,300.636261]],
                [['RTOmniLight18'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[409.259003,-458.469635,300.636261]],
                [['RTOmniLight19'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[421.618042,-447.845062,300.636261]],
                [['RTOmniLight20'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[400.238190,-435.353607,300.636261]],
                [['RTOmniLight21'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[439.385254,-366.252411,300.636261]],
                [['RTOmniLight22'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[461.506775,-378.483063,300.636261]],
                [['RTOmniLight23'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[325.963837,-490.661102,252.551651]],
                [['RTPathLight'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[735.054199,-456.368805,263.444885]],
                [['RTPathLight01'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[750.834961,-472.354797,263.444885]],
                [['RTPathLight02'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[733.413086,-489.621643,263.444885]],
                [['RTPathLight03'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[719.006958,-472.543671,263.444885]],
                [['RTPathLight04'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[733.147217,-519.070068,263.444885]],
                [['RTPathLight05'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[716.766113,-534.463989,263.444885]],
                [['RTPathLight06'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[736.000000,-553.463257,263.444885]],
                [['RTPathLight07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[751.709229,-537.602783,263.444885]],
                [['RTPathLight08'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[734.336609,-608.917236,271.064392]],
                [['RTPathLight09'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[811.764465,-539.207214,271.064392]],
                [['RTPathLight10'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[716.646545,-652.480957,271.064392]],
                [['RTPathLight11'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[871.652100,-527.806213,271.064392]],
                [['RTPathLight12'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[757.704468,-435.586182,283.911591]],
                [['RTPathLight13'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[773.331238,-450.557281,283.911591]],
                [['RTPathLight14'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[795.815918,-428.989471,304.255676]],
                [['RTPathLight15'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[779.921631,-412.855774,304.255676]],
                [['RTPathLight16'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[771.412415,-358.311707,304.255676]],
                [['RTPathLight17'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[783.410583,-339.409546,304.255676]],
                [['RTPathLight18'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[694.166809,-353.117615,304.255676]],
                [['RTPathLight19'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[698.438660,-331.243042,304.255676]],
                [['RTPathLight20'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[645.806763,-287.588684,304.255676]],
                [['RTPathLight21'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[626.672241,-299.529816,304.255676]],
                [['RTPathLight22'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[598.299500,-225.519028,304.255676]],
                [['RTPathLight23'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[582.089905,-241.262375,304.255676]],
                [['RTPathLight24'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[561.777771,-222.303864,304.255676]],
                [['RTPathLight25'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[586.824890,-212.537369,304.255676]],
                [['RTPathLight26'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[537.860046,-205.031815,304.255676]],
                [['RTPathLight27'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[459.639008,-91.621437,304.255676]],
                [['RTPathLight28'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[471.849487,-72.576752,304.255676]],
                [['RTOmniWeldLight'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-3.959454,218.842453,476.568268]],
                [['RTPalaceYllwLight02'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[111.216782,3.297459,265.175964]],
                [['RTPalaceYllwLight03'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[227.587128,59.269970,295.968292]],
                [['RTPalaceYllwLight04'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[388.763611,-89.193802,264.769623]],
                [['RTPalaceYllwLight05'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[397.553619,-109.853455,264.769623]],
                [['RTRedLight'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-159.317581,-498.027374,32.851402]],
                [['pierorangecone14'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-219.892883,-519.432495,9.709713]],
                [['pierorangecone15'],[0.996932,-0.078265,-0.001357],[0.001422,0.000774,0.999999],[-238.097366,-529.646057,9.761376]],
                [['orangecone'],[0.293721,0.955891,0.000444],[-0.000273,-0.000380,1.000000],[115.823029,-158.646988,216.309830]]),
        # Use this to Create a Nuclear Powerplant With some city cones
        # This will be placed near the Courtyard tent
        'powerplant' : ([['orangecone02'],[-15.900290,12.131454,0.092940],[-0.007893,-0.163562,19.999331],[-77.663223,-99.565887,227.672668],[20,20,20]],
                [['orangecone04'],[2.278535,7.667797,0.114785],[0.070719,-0.140750,7.998450],[-65.988556,-97.189606,227.669144],[6,6,6]],
                [['orangecone05'],[-3.917741,0.806216,-0.036327],[-0.042142,-0.024565,3.999703],[-67.223053,-95.248230,225.661819],[4,4,4]],
                [['orangecone07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,15.000000],[-66.727570,-97.956909,221.672668],[1,1,20]],
                [['smokeemitter01'],[0.000000,-0.788011,-0.615662],[0.000000,-0.615662,0.788011],[-70.600494,-99.382484,255.673111]],
                [['smokeemitter02'],[-0.190051,-0.791621,-0.580703],[-0.135562,-0.564658,0.814115],[-72.600494,-103.382484,247.673111]]),
        # puts a small arch on the table in front of the library tent
        'archlibtent' : ([['ArchOfKerath'],[-0.003536,-0.003536,0.000000],[0.000000,0.000000,0.005000],[833.847717,-556.203125,262.493945],[0.005000,0.005000,0.005000]],),
        # turns the shroomiepicture into a carpet for the courtyard. This command may need to be run twice.
        'shroomiecarpet' : ([['ShroomiePict'],[0.000000,-40.000000,0.000000],[0.000000,0.000000,40.000000],[-64.589180,-90.958916,221.798233],[40.000000,40.000000,40.000000]],),
        # turns the you are here map into a carpet
        'mcarpet' : ([['MapBoard'],[4.582931,-4.924449,7.399114],[-8.497411,-4.868424,2.023039],[1256.353027,2097.654297,-166.529449],[10,10,10]],),
        # create a small bridal arch next to the Treebolisk
        'bridearch' : ([['ArchOfKerath'],[-0.069751,0.005899,0.000000],[0.000000,0.000000,0.070000],[-29.251051,-87.343681,221.682053],[0.07,0.07,0.07]],),
        # Weldergeek's D'ni Torch
        # Located at the bottom of the stairs by the library
        'torch' : ([['OrangeCone'],[-0.562198,-0.827000,-0.002092],[-0.001136,-0.001757,0.999998],[724.834290,-489.673584,270.156616]],
                [['OrangeCone01'],[-3.105758,2.520766,-0.002565],[0.000665,-0.003250,-3.999999],[719.107239,-487.686340,262.656189],[4,4,4]],
                [['OrangeCone05'],[-0.982196,-0.187837,-0.002986],[-0.002764,-0.001444,0.999995],[718.859802,-492.832916,270.066956]],
                [['OrangeCone10'],[0.997760,0.066849,0.002473],[-0.002292,-0.002785,0.999994],[722.742310,-483.829498,270.150635]],
                [['OrangeCone10b'],[0.843802,0.536651,-0.002057],[0.000403,0.003200,0.999995],[716.291870,-487.640869,270.028900]],
                [['ArchOfKerath'],[0.005380,0.005225,0.000000],[0.000000,0.000000,0.007500],[720.798401,-488.072632,269.656860],[0.0075,0.0075,0.0075]],
                [['SmokeEmitter01'],[0.000000,-0.989172,-0.146764],[0.000000,-0.146764,0.989172],[721.455261,-486.344727,267.670410]]),
        'torch2' : ([['OrangeCone'],[-0.562198,-0.827000,-0.002092],[-0.001136,-0.001757,0.999998],[724.834290,-489.673584,270.156616]],
                [['OrangeCone01'],[-3.105758,2.520766,-0.002565],[0.000665,-0.003250,-3.999999],[719.107239,-487.686340,262.656189],[4,4,4]],
                [['OrangeCone05'],[-0.982196,-0.187837,-0.002986],[-0.002764,-0.001444,0.999995],[718.859802,-492.832916,270.066956]],
                [['OrangeCone10'],[0.997760,0.066849,0.002473],[-0.002292,-0.002785,0.999994],[722.742310,-483.829498,270.150635]],
                [['OrangeCone10b'],[0.843802,0.536651,-0.002057],[0.000403,0.003200,0.999995],[716.291870,-487.640869,270.028900]],
                [['ArchOfKerath'],[0.005380,0.005225,0.000000],[0.000000,0.000000,0.007500],[720.798401,-488.072632,268.456848],[0.0075,0.0075,0.0075]],
                [['SmokeEmitter01'],[0.000000,-0.989172,-0.146764],[0.000000,-0.146764,0.989172],[721.455261,-486.344727,267.670410]]),
        # Drakmyth's City Conecano
        # Covers the tree in the Tokotah Courtyard
        'citycano' : ([['OrangeCone'],[-56.219803,-82.700012,-0.209200],[-0.113617,-0.175725,99.999786],[-26.159983,-87.262367,226.933777],[100,100,100]],
                [['SmokeEmitter01'],[0.000000,-0.989172,-0.146764],[0.000000,-0.146764,0.989172],[21.377424,-92.813759,334.944214]],
                [['SmokeEmitter02'],[-0.190051,-0.791621,-0.580703],[-0.135562,-0.564659,0.814115],[11.377424,-92.813759,336.944214]],
                [['RTOmniWeldLight'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,334.932373]],
                [['RTOmniLight01'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,334.932373]],
                [['RTOmniLight02'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,336.932373]],
                [['RTOmniLight03'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,338.932373]],
                [['RTOmniLight04'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,340.932373]],
                [['RTOmniLight05'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,342.932373]],
                [['RTOmniLight06'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,344.932373]],
                [['RTOmniLight07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,346.932373]],
                [['RTOmniLight08'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,348.932373]],
                [['RTOmniLight09'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,350.932373]],
                [['RTOmniLight10'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,352.932373]],
                [['RTOmniLight11'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,354.932373]],
                [['RTOmniLight12'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,356.932373]],
                [['RTOmniLight13'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,358.932373]],
                [['RTOmniLight14'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,360.932373]],
                [['RTOmniLight15'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,362.932373]],
                [['RTOmniLight16'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,364.932373]],
                [['RTOmniLight17'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,366.932373]],
                [['RTOmniLight18'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,368.932373]],
                [['RTOmniLight19'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,370.932373]],
                [['RTOmniLight20'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,372.932373]],
                [['RTOmniLight21'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,374.932373]],
                [['RTOmniLight22'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,376.932373]],
                [['RTOmniLight23'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[16.413231,-90.736000,378.932373]]),
        # Drakmyth's Great Conehenge
        # Adaptation of Conehenge featuring the Great Cone at its center
        'conehenge2' : ([['ALYOrangeCone12'],[-0.838671,0.544639,0.000000],[0.000000,0.000000,1.000000],[107.600616,-149.025574,216.297729]],
                [['ALYOrangeCone11'],[-0.998630,0.052336,0.000000],[0.000000,0.000000,1.000000],[111.763214,-147.583282,216.308990]],
                [['ALYOrangeCone10'],[-0.173648,-0.984808,0.000000],[0.000000,0.000000,1.000000],[115.838974,-148.098953,216.307770]],
                [['OrangeCone11b'],[-0.927184,0.374607,0.000000],[0.000000,0.000000,1.000000],[120.209511,-149.094345,216.300583]],
                [['OrangeCone06b'],[-0.999391,-0.034899,0.000000],[0.000000,0.000000,1.000000],[123.516808,-151.815659,216.304367]],
                [['OrangeCone19'],[-0.996195,-0.087156,0.000000],[0.000000,0.000000,1.000000],[125.316269,-156.613358,216.304962]],
                [['OrangeCone18'],[0.104529,-0.994522,0.000000],[0.000000,0.000000,1.000000],[126.063583,-161.692444,216.308655]],
                [['OrangeCone12'],[-1.000000,0.000000,0.000000],[0.000000,0.000000,1.000000],[124.652817,-165.750656,216.302338]],
                [['OrangeCone10'],[0.258819,-0.965926,0.000000],[0.000000,0.000000,1.000000],[121.027451,-169.761230,216.303864]],
                [['OrangeCone09'],[-0.173648,-0.984808,0.000000],[0.000000,0.000000,1.000000],[116.636932,-171.568680,216.300629]],
                [['OrangeCone08'],[0.518212,0.660321,0.543536],[0.854879,-0.381149,-0.352006],[111.843849,-170.985260,216.295181]],
                [['OrangeCone05'],[-0.587785,0.809017,0.000000],[0.000000,0.000000,1.000000],[107.732079,-169.330261,216.298965]],
                [['OrangeCone04'],[-0.213987,-0.960290,0.179033],[-0.926681,0.141588,-0.348159],[104.879921,-167.415314,216.293716]],
                [['OrangeCone03'],[0.087156,0.996195,0.000000],[0.000000,0.000000,1.000000],[102.954956,-162.775864,216.309418]],
                [['OrangeCone01'],[0.469472,0.882948,0.000000],[0.000000,0.000000,1.000000],[102.405106,-157.952698,216.303970]],
                [['OrangeCone'],[1.294095,4.829629,0.000000],[0.000000,0.000000,5.000000],[115.503761,-158.615219,221.308807],[5,5,5]]),
        # Presentation Stage (Tokotah Courtyard)
        # don't forget to use freeze toggle (/struct ostage 1)
        # or someone may kick the stage away
        # Now with Solid Floor (the cones)
        # to use with /Structhere you need to freeze yourself and drop 4
        'ostage' :  ([['OrangeCone02'],[0.335603,-0.942001,0.002236],[0.003504,-0.001125,-0.999993],[-67.310661,-74.898476,220.746811]],
                [['OrangeCone'],[0.418422,0.908248,0.002832],[0.002527,0.001954,-0.999995],[-73.615265,-73.926361,220.723465]],
                [['OrangeCone01'],[-0.944882,-0.327405,-0.001873],[0.001686,0.000855,-0.999998],[-70.875786,-74.703941,220.800674]],
                [['OrangeCone03'],[-0.947070,-0.321022,-0.001741],[0.001091,0.002204,-0.999997],[-73.513412,-77.242165,220.908264]],
                [['OrangeCone04'],[-0.329290,0.944220,0.004161],[-0.000730,0.004152,-0.999991],[-72.942688,-65.341919,220.908478]],
                [['OrangeCone05'],[-0.330493,0.943803,0.003114],[0.000918,0.003621,-0.999993],[-70.471832,-65.534004,220.811478]],
                [['OrangeCone06'],[0.006293,0.994324,0.106206],[0.926815,-0.045678,0.372730],[-67.436234,-66.369469,220.708160]],
                [['OrangeCone06b'],[-0.515146,0.857102,0.000766],[-0.000291,0.000719,-1.000000],[-70.854500,-77.479614,220.821640]],
                [['OrangeCone07'],[-0.947188,-0.320679,-0.000421],[0.001149,-0.002080,-0.999997],[-73.244812,-68.901115,220.915787]],
                [['OrangeCone07b'],[-0.914787,0.403937,0.000896],[-0.002663,-0.003813,-0.999989],[-70.502190,-68.498909,220.898865]],
                [['OrangeCone08'],[-0.331852,0.943331,-0.000175],[-0.001155,-0.000592,-0.999999],[-67.851730,-68.698219,220.720383]],
                [['OrangeCone08b'],[-0.984732,-0.174068,0.001890],[-0.001703,-0.001224,-0.999998],[-67.956375,-77.726547,220.739349]],
                [['OrangeCone09'],[-0.944700,-0.327933,-0.001444],[0.002781,-0.003607,-0.999990],[-73.478035,-71.691109,221.010406]],
                [['OrangeCone09b'],[-0.868570,0.495563,0.001808],[-0.000863,0.002135,-0.999997],[-70.766632,-71.947929,220.916794]],
                [['OrangeCone10'],[0.325810,-0.945435,0.001146],[0.000470,-0.001050,-0.999999],[-67.195671,-72.249214,220.785538]],
                [['OrangeCone10b'],[0.208530,0.978012,-0.002779],[-0.001719,-0.002475,-0.999996],[-73.646141,-80.111031,220.814987]],
                [['orangecone11'],[0.541553,-0.338239,-0.769620],[-0.067496,-0.930026,0.361241],[-70.985138,-80.342430,221.004608]],
                [['orangecone11b'],[-0.961264,0.275630,-0.000081],[0.000207,0.000428,-1.000000],[-67.940117,-80.519684,220.813446]],
                [['orangecone12'],[0.592568,0.805520,-0.000995],[-0.000447,-0.000906,-1.000000],[-73.856094,-83.061089,221.015549]],
                [['orangecone19'],[-0.050260,0.998736,0.000992],[0.001567,0.001072,-0.999998],[-70.414299,-82.769852,221.005112]],
                [['alyorangecone10'],[0.096251,0.995353,0.002764],[0.000429,0.002735,-0.999996],[-68.286171,-83.047241,220.899292]],
                [['alyorangecone11'],[-0.149129,0.988815,-0.002355],[0.001023,-0.002227,-0.999997],[-73.976280,-85.112343,220.905106]],
                [['alyorangecone12'],[0.595806,0.803129,0.000089],[-0.000236,0.000286,-1.000000],[-70.704994,-85.736755,220.909958]],
                [['alyorangecone13'],[0.233497,-0.367605,0.900192],[0.117298,0.929671,0.349218],[-67.901009,-86.583588,220.920486]]),

        # Art done by Lord Chaos turned into a structure by ShadowDude
        'lordchaos1' : ([['OrangeCone'],[-0.970322,0.241793,-0.003400],[-0.002906,0.002401,0.999993],[120.212242,-150.804443,216.303284]],
                [['OrangeCone01'],[0.893895,-0.448273,-0.002030],[-0.000297,-0.005121,0.999987],[117.649292,-150.843964,216.302094]],
                [['OrangeCone02'],[0.985913,0.167254,0.001024],[-0.001442,0.002375,0.999996],[114.836205,-151.572220,216.306488]],
                [['OrangeCone03'],[0.250614,0.968087,-0.000155],[0.002193,-0.000407,0.999997],[103.592453,-160.391846,216.306290]],
                [['OrangeCone04'],[0.346739,-0.716441,-0.605380],[0.477040,0.690412,-0.543842],[157.897400,-269.898590,-2000.223511]],
                [['OrangeCone05'],[0.986443,0.164103,0.000089],[0.000341,-0.002589,0.999997],[107.882927,-150.705444,216.300919]],
                [['OrangeCone06'],[-0.563809,0.818863,-0.107622],[-0.747391,-0.561313,-0.355435],[104.531670,-164.036606,216.304764]],
                [['OrangeCone06b'],[-0.907282,-0.420517,0.002153],[0.002698,-0.000701,0.999996],[103.691727,-154.664566,216.307938]],
                [['OrangeCone07'],[-0.473769,-0.880649,0.000630],[0.000405,0.000498,1.000000],[102.813225,-158.240204,216.310013]],
                [['OrangeCone07b'],[0.363375,0.931642,-0.001222],[0.002149,0.000474,0.999998],[106.554420,-165.044495,216.305054]],
                [['OrangeCone08'],[-0.153254,-0.988185,0.001679],[0.002625,0.001292,0.999996],[111.610497,-157.297775,216.303680]],
                [['OrangeCone08b'],[-0.001290,-0.999995,-0.002802],[0.002327,-0.002805,0.999993],[115.398064,-162.373154,216.306854]],
                [['OrangeCone09'],[0.665832,-0.746101,0.000040],[-0.002671,-0.002331,0.999994],[112.494171,-154.242523,216.301361]],
                [['OrangeCone09b'],[-0.592291,0.805723,-0.001715],[-0.004373,-0.001086,0.999990],[112.497635,-166.480103,216.305435]],
                [['OrangeCone10'],[-0.780822,0.624753,-0.001076],[-0.000459,0.001148,0.999999],[109.039207,-166.419525,216.306244]],
                [['OrangeCone10b'],[0.827167,-0.561957,0.000350],[-0.000671,-0.000365,1.000000],[113.294083,-159.340179,216.309021]],
                [['OrangeCone11'],[0.647319,-0.165628,0.744007],[0.594783,0.720187,-0.357162],[115.024338,-164.853882,216.308823]],
                [['OrangeCone11b'],[-0.453717,-0.891146,0.000612],[0.000628,0.000368,1.000000],[122.479149,-166.502747,216.309784]],
                [['OrangeCone12'],[-0.374548,-0.927207,-0.000761],[0.000358,-0.000965,0.999999],[120.887642,-168.025116,216.309586]],
                [['OrangeCone18'],[0.206711,-0.978402,0.000924],[-0.000539,0.000831,1.000000],[125.204903,-161.401062,216.309998]],
                [['OrangeCone19'],[-0.525864,-0.850569,0.000042],[0.000237,-0.000097,1.000000],[124.383644,-164.302612,216.309982]],
                [['ALYOrangeCone10'],[0.992530,0.121945,-0.003669],[0.003633,0.000516,0.999993],[125.194595,-158.618698,216.301498]],
                [['ALYOrangeCone11'],[0.416780,-0.909000,0.003716],[-0.002599,0.002896,0.999992],[122.409180,-153.580490,216.303680]],
                [['ALYOrangeCone12'],[-0.534803,-0.844976,0.000857],[-0.000514,0.001340,0.999999],[123.800804,-155.907196,216.301788]],
                [['ALYOrangeCone13'],[0.053911,-0.452269,-0.890251],[-0.714499,0.605339,-0.350795],[105.400558,-152.955551,216.306396]]),
        #By Greypiffle Fogg
        # turn off the physics for the citycones when you make this structure
        #here is a nice one I got done. It cerates a circle of upside down cones in the air for people
        #to sit on and walk on.  You can jump onto the tent from them, or jump on them from the tent
        'cconewalk' : ([['OrangeCone01'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-63.899277,-92.013733,230.678741]],
                [['OrangeCone02'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-65.397789,-88.396011,230.678741]],
                [['OrangeCone03'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-67.781578,-85.289406,230.678741]],
                [['OrangeCone04'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-70.888191,-82.905624,230.678741]],
                [['OrangeCone05'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-74.505920,-81.407127,230.678741]],
                [['OrangeCone06'],[-0.233251,0.957262,0.171010],[0.925554,0.164615,0.340957],[-77.372452,-81.049591,230.678726]],
                [['OrangeCone06b'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-82.270508,-81.407158,230.678741]],
                [['OrangeCone07'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-85.888222,-82.905685,230.678741]],
                [['OrangeCone07b'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-88.994820,-85.289482,230.678741]],
                [['OrangeCone08'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-91.378586,-88.396103,230.678741]],
                [['OrangeCone08b'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-92.877075,-92.013840,230.678741]],
                [['OrangeCone09'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-93.388161,-95.896133,230.678741]],
                [['OrangeCone09b'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-92.877014,-99.778427,230.678741]],
                [['OrangeCone10'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-91.378479,-103.396133,230.678741]],
                [['OrangeCone10b'],[0.000000,1.000000,-0.000000],[0.173648,-0.000000,-0.984808],[-88.994659,-106.502724,230.678757]],
                [['OrangeCone11'],[-0.469846,0.342020,-0.813798],[0.171010,0.939693,0.296198],[-85.776443,-108.994354,230.678741]],
                [['OrangeCone11b'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-82.270302,-110.384956,230.678741]],
                [['OrangeCone12'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-78.387993,-110.896027,230.678741]],
                [['OrangeCone18'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-74.505707,-110.384872,230.678741]],
                [['OrangeCone19'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-70.888000,-108.886314,230.678741]],
                [['ALYOrangeCone10'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-67.781425,-106.502495,230.678741]],
                [['ALYOrangeCone11'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-65.397682,-103.395859,230.678741]],
                [['ALYOrangeCone12'],[0.000000,1.000000,-0.000000],[0.000000,-0.000000,-1.000000],[-63.899220,-99.778107,230.678741]],
                [['ALYOrangeCone13'],[0.422618,-0.339509,0.840314],[-0.000000,0.927184,0.374607],[-63.296307,-96.803345,230.678741]]),

# By Diafero
        'coneheart': ([['ALYOrangeCone12'],[-0.995700,0.092637,-0.000769],[-0.000743,0.000312,1.000000],[109.592964,-149.413055,216.295929]],
                [['ALYOrangeCone11'],[-0.967604,0.252472,-0.000338],[-0.000694,-0.001323,0.999999],[116.205635,-171.977219,216.296539]],
                [['ALYOrangeCone10'],[-0.426820,-0.904337,0.000235],[0.000134,0.000197,1.000000],[114.168213,-148.329376,216.303421]],
                [['OrangeCone11b'],[-0.846175,0.532905,0.000131],[-0.001124,-0.002029,0.999997],[118.959831,-149.617096,216.294693]],
                [['OrangeCone06b'],[-0.986844,0.161675,0.000684],[0.000645,-0.000290,1.000000],[121.893311,-152.897064,216.295685]],
                [['OrangeCone19'],[-0.520572,-0.853817,-0.000531],[-0.000947,-0.000045,1.000000],[124.680344,-157.947357,216.293274]],
                [['OrangeCone18'],[0.591647,-0.806194,-0.002116],[0.005853,0.001671,0.999981],[127.672386,-161.446915,216.301529]],
                [['OrangeCone12'],[0.195446,0.980714,-0.000951],[0.001188,0.000733,0.999999],[129.206436,-166.292023,216.307205]],
                [['OrangeCone10'],[0.993717,-0.111916,-0.000497],[0.000344,-0.001391,0.999999],[125.898010,-170.552933,216.296570]],
                [['OrangeCone09'],[0.866024,-0.499982,-0.004563],[0.003228,-0.003536,0.999989],[121.584229,-171.516266,216.298508]],
                [['OrangeCone08'],[0.761518,-0.351444,0.544589],[-0.174808,-0.920459,-0.349566],[111.273735,-171.015381,216.295059]],
                [['OrangeCone05'],[-0.979479,0.201526,-0.002897],[-0.002367,0.002874,0.999993],[105.919472,-168.721115,216.298172]],
                [['OrangeCone04'],[0.846608,-0.501683,0.177677],[-0.422841,-0.836768,-0.347887],[111.366089,-158.842880,216.295502]],
                [['OrangeCone03'],[-0.291003,0.956721,-0.001277],[-0.002116,0.000692,0.999997],[102.692345,-164.800339,216.309113]],
                [['OrangeCone01'],[0.828443,-0.560059,-0.003982],[0.004008,-0.001182,0.999991],[106.677505,-162.016266,216.302231]],
                [['OrangeCone'],[0.965867,0.259037,0.000836],[-0.000197,-0.002493,0.999997],[110.203896,-155.200897,216.296722]]),
    },

    'Teledahn' : {
        # Telescope camera in fishtank room. Example with view of self.
        'officescope1' : ([['telescopecamera.Target'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-116.881035,-220.029541,137.504181]],
                [['telescopecamera'],[0.000000,0.000000,-1.000000],[0.915964,0.401261,0.000000],[-107.845757,-216.734970,137.504227]]),
        # The Power Tower Telescope camera (sun-tracker), complete with working controls.
        # Set to view the desk area in office of upper shroom
        'towerscope1' : ([['CamPwrTwrPeriscope.Target'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-103.889236,-213.998016,137.513565]],
                [['CamPwrTwrPeriscope'],[0.000000,0.170226,-0.985405],[0.000000,0.985405,0.170226],[-110.774757,-221.156799,137.515411]]),
    },

    'Neighborhood' : {
        # Warps laptop to fountain, camcorder to heek table and Box to telescope steps.
        #Use this command twice to properly warp laptop to correct location...(possible bug with object)
        'electronics' : ([['VidCamLaptop'],[0.984808,-0.173648,0.000000],[0.000000,0.000000,1.000000],[292.665527,-803.494446,4.807072]],
                [['VidCamBody'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-54.000000,-66.000000,-23.000000]],
                [['VidCamBox'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[12.000000,-30.000000,0.000000]]),
        # Camera points to speaker area in Community Room
        'hoodscope1' : ([['BevinTeleCam.Target'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[324.079529,-675.063904,20.125578]],
                [['BevinTeleCam'],[0.000000,0.000000,-1.000000],[-1.000000,0.000000,0.000000],[308.033203,-711.985413,25.116673]]),
        # Camera points to the Bahro Stone on Balcony
        'hoodscope2' : ([['BevinTeleCam.Target'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[22.871246,-795.275330,84.965500]],
                [['BevinTeleCam'],[0.000000,0.000000,-1.000000],[-1.000000,0.000000,0.000000],[47.507507,-791.025757,84.965500]]),
        # Camera Points over most of the Hood
        'hoodscope3' : ([['BevinTeleCam'],[0.000000,0.000000,-1.000000],[-1.000000,0.000000,0.000000],[357.356018,-733.281921,153.593658]],
                [['BevinTeleCam.Target'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[29.276581,-793.028748,94.593658]]),
        # Camera points over the Lush Garden
        'hoodscope4' : ([['BevinTeleCam'],[0.000000,0.000000,-1.000000],[-1.000000,0.000000,0.000000],[147.400574,-947.086914,18.621449]],
                [['BevinTeleCam.Target'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[136.410751,-910.741394,9.621449]]),
        # Camera Points down at Egg, in Private room
        'hoodscope5' : ([['BevinTeleCam'],[0.000000,0.000000,-1.000000],[-1.000000,0.000000,0.000000],[-10.091766,-769.004456,29.597744]],
                [['BevinTeleCam.Target'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[-10.249512,-768.016968,23.597744]]),
        # Camera points from Under Water near garden
        'hoodscope6' : ([['BevinTeleCam'],[0.000000,0.000000,-1.000000],[-1.000000,0.000000,0.000000],[146.240799,-774.700867,-20.513968]],
                [['BevinTeleCam.Target'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[153.982956,-837.060303,-20.513968]]),
        # Camera points from atop of link room facing the Walkways
        'hoodscope7' : ([['BevinTeleCam'],[0.000000,0.000000,-1.000000],[-1.000000,0.000000,0.000000],[117.068161,-761.474854,35.431175]],
                [['BevinTeleCam.Target'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[174.875061,-793.323853,35.431175]]),
        # The /cleanhood command converted to structure list. Now includes the fireworks.
        'cleanhood' : ([['OrangeCone01'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[92.460808,-802.809875,9.517658]],
                [['OrangeCone04'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[86.096725,-792.269958,9.534151]],
                [['OrangeCone05'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[92.365799,-815.000610,9.521742]],
                [['OrangeCone11'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[236.843430,-801.102539,3.958330]],
                [['OrangeCone12'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[239.598877,-804.692261,3.968128]],
                [['OrangeCone15'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[232.847427,-808.622620,3.961110]],
                [['OrangeCone16'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[193.496109,-850.791199,-17.103058]],
                [['OrangeCone17'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[196.706802,-856.860779,-17.073460]],
                [['MarblePhy06'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[77.151566,-775.497620,10.544244]],
                [['MarblePhy07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[74.142410,-795.187439,10.544244]],
                [['MarblePhy08'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[135.593857,-812.488342,10.544244]],
                [['Pumpkin01'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[261.422821,-841.901428,3.946658]],
                [['Pumpkin02'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[282.188965,-833.086121,3.772740]],
                [['BeachBall'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[246.821274,-795.803650,4.189516]],
                [['SparklerEmit01'],[0.901219,0.433313,-0.006685],[-0.273925,0.581537,0.766015],[285.386871,-841.269043,23.434849]],
                [['SparklerEmit02'],[0.901219,0.433313,-0.006685],[-0.273925,0.581537,0.766015],[265.490570,-850.352478,23.434839]],
                [['SparklerEmit03'],[-0.999712,0.023060,-0.006685],[-0.019943,-0.642513,0.766015],[279.463684,-763.924255,22.897312]],
                [['SparklerEmit04'],[-0.311973,0.950067,-0.006685],[-0.612316,-0.195676,0.766015],[307.065491,-780.735229,22.897327]],
                [['SprayEmit'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,-1.000000],[280.016113,-796.967773,9.733724]]),
        # The HoodStar - ConeStar's little brother - 04-03-2005
        'hoodstar' : ([['OrangeCone01'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[280.016113,-796.967773,10.333724]],
                [['OrangeCone04'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,-1.000000],[280.016113,-796.967773,12.903702]],
                [['OrangeCone05'],[0.000000,0.000000,1.000000],[0.000000,1.000000,0.000000],[280.016113,-798.258545,11.533705]],
                [['OrangeCone11'],[0.000000,0.000000,-1.000000],[0.000000,-1.000000,0.000000],[280.016113,-795.667786,11.533705]],
                [['OrangeCone12'],[0.000000,-1.000000,0.000000],[1.000000,0.000000,0.000000],[278.881042,-796.822693,11.533705]],
                [['OrangeCone15'],[0.000000,-1.000000,0.000000],[-1.000000,0.000000,0.000000],[281.455872,-796.822693,11.533705]],
                [['OrangeCone16'],[0.179030,-0.983844,0.000000],[0.000000,0.000000,1.000000],[280.016113,-796.967773,15.542068]]),
        # HoodStar with fireworks from the top cone. - 04-03-2005
        'hoodstar2' : ([['OrangeCone01'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[280.016113,-796.967773,10.333724]],
                [['OrangeCone04'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,-1.000000],[280.016113,-796.967773,12.903702]],
                [['OrangeCone05'],[0.000000,0.000000,1.000000],[0.000000,1.000000,0.000000],[280.016113,-798.258545,11.533705]],
                [['OrangeCone11'],[0.000000,0.000000,-1.000000],[0.000000,-1.000000,0.000000],[280.016113,-795.667786,11.533705]],
                [['OrangeCone12'],[0.000000,-1.000000,0.000000],[1.000000,0.000000,0.000000],[278.881042,-796.822693,11.533705]],
                [['OrangeCone15'],[0.000000,-1.000000,0.000000],[-1.000000,0.000000,0.000000],[281.455872,-796.822693,11.533705]],
                [['OrangeCone16'],[0.179030,-0.983844,0.000000],[0.000000,0.000000,1.000000],[280.016113,-796.967773,15.542068]],
                [['SprayEmit'],[0.000000,-1.000000,0.000000],[0.000000,-0.000000,-1.000000],[280.016113,-796.967773,16.033724]]),

        # Christmas Tree made out of hood objects
        'xmastree' : ([['OrangeCone01'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[280.917908,-796.075012,9.641020]],
                [['OrangeCone04'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[280.037476,-795.700623,9.641020]],
                [['OrangeCone05'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[279.150208,-796.058533,9.641020]],
                [['OrangeCone11'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[278.775879,-796.938904,9.641020]],
                [['OrangeCone12'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[279.133698,-797.826172,9.641020]],
                [['OrangeCone15'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[280.014160,-798.200500,9.641020]],
                [['OrangeCone16'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[280.901398,-797.842651,9.641020]],
                [['OrangeCone17'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[281.275757,-796.962280,9.641020]],
                [['Beachball'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[280.025818,-796.950562,11.640566]],
                [['MarblePhy06'],[-0.009315,-0.999957,0.000000],[0.000000,0.000000,1.000000],[280.025818,-796.950562,15.641022]],
                [['MarblePhy07'],[-0.009315,-0.999957,0.000000],[0.000000,0.000000,1.000000],[280.025818,-796.950562,15.641022]],
                [['MarblePhy08'],[-0.009315,-0.999957,0.000000],[0.000000,0.000000,1.000000],[280.025818,-796.950562,15.641022]],
                [['Pumpkin01'],[-0.009342,-0.999957,0.000000],[0.000000,0.000000,1.000000],[280.025818,-796.950562,13.640566]],
                [['Pumpkin02'],[-1.000000,0.000000,0.000000],[0.000000,0.000000,1.000000],[279.982056,-796.766479,14.609295]],
                [['SprayEmit'],[0.0,-1.0,0.0],[0.0,0.0,-1.0],[280.01611300000002,-796.96777299999997,9.7337240000000005]]),

        # This Structure for the Hood Is bound to make your stomach turn
        'hoodflip' : ([['nb01DistantCityFake-Group'],[0.707107,-0.707107,0.000000],[0.000000,-0.000000,-1.000000],[-2371.371094,-829.174866,1210.000000]],),
        # conecano -) 3/6/2005 (- ##
        # a nice piece of destructive power for the hood :)
        # After it's up turn on the fireworks
        'conecano' : ([['pumpkin01'],[0.000000,-49.735592,0.005135],[0.000000,5.135301,0.049736],[280.126068,-796.597656,2.496385],[50,50,.05]],
                [['pumpkin02'],[0.000000,-60.000000,0.000000],[0.000000,0.000000,5.000000],[277.279846,-801.013489,3.214544],[60,60,5]],
                [['orangecone01'],[0.000000,-45.000000,0.000000],[0.000000,0.000000,15.000000],[279.404877,-797.841919,6.717097],[45,45,15]],
                [['sprayemit'],[0.000000,-5.000000,0.000000],[0.000000,0.000000,-1.000000],[280.016113,-796.967773,19.733723],[5,5,1]]),
        ## PUMPKINMAN STRUCTURE ##
        'pumpkinman' : (
                # Give this one a try, You are sure to love it
                # Enjoy it, and let us know ur thoughts
                # LOWER BODY AND LEGS
                [['orangecone05'],[0.000000,1.000000,-0.000000],[0.573577,-0.000000,-4.095760],[251.460129,-803.643860,8.602579],[1.0,1.0,5.0]],
                [['orangecone11'],[0.000000,1.000000,-0.000000],[-0.573577,-0.000000,-4.095760],[245.460129,-803.643860,8.602579],[1.0,1.0,5.0]],
                [['orangecone04'],[0.000000,4.000000,-0.000000],[0.000000,-0.000000,-4.000000],[248.529037,-803.386475,12.608671],[4.0,4.0,4.0]],
                # HAT
                [['orangecone01'],[3.649006,1.638459,0.014310],[0.416453,-0.961196,3.860398],[249.741821,-807.023682,40.599236],[4.0,4.0,4.0]],
                # HEAD AND MOUTH
                [['pumpkin01'],[0.000000,-3.464102,-2.000000],[0.000000,-2.000000,3.464102],[248.198593,-805.222412,33.600723],[4.0,4.0,4.0]],
                [['beachball'],[0.002706,0.992781,0.119822],[-0.015103,0.119931,-0.992323],[248.064056,-807.100891,29.599613],[0.5,1.0,1.0]],
                # EYES, NO SCALE
                [['marblephy06'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[249.727829,-809.754272,30.601421]],
                [['marblephy07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[245.827835,-809.454224,30.601421]],
                # SPINE OR BACKBONE
                [['orangecone17'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,10.000000],[248.460129,-803.643860,19.602579],[1.0,1.0,10.0]],
                # UPPER BODY AND ARMS
                [['orangecone12'],[-3.939231,-0.694593,-0.000000],[0.000000,-0.000000,4.000000],[248.460129,-803.643860,22.602579],[4.0,4.0,4.0]],
                [['orangecone15'],[0.000000,-1.000000,0.000000],[5.000000,0.000000,-0.000000],[251.460129,-803.643860,24.602579],[5.0,1.0,1.0]],
                [['orangecone16'],[0.000000,-1.000000,0.000000],[-5.000000,0.000000,0.000000],[245.460129,-803.643860,24.602579],[5.0,1.0,1.0]]),
        # A work in progress
        'pumpkinhead' : ([['Pumpkin01'],[0.000000,-4.000000,0.000000],[0.000000,0.000000,4.000000],[280.763458,-796.776428,11.144613],[4.000000,4.000000,4.000000]],
                [['MarblePhy06'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[275.568909,-796.182190,11.603234]],
                [['MarblePhy07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,1.000000],[277.368896,-800.082214,11.603234]],
                [['BeachBall'],[0.043486,0.997240,0.060180],[-0.438313,0.073174,-0.895839],[277.189911,-798.053650,9.485018]],
                [['OrangeCone01'],[3.649006,1.638459,0.014310],[-0.007892,-0.017359,3.999955],[280.919861,-796.963074,19.017250],[4.000000,4.000000,4.000000]]),
        'fountainbeams' : (
                [['MarblePhy06'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,20.000000],[277.922577,-806.650574,9.138309],[1.000000,1.000000,20.000000]],
                [['MarblePhy07'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,20.000000],[286.382660,-804.719482,9.138309],[1.000000,1.000000,20.000000]],
                [['MarblePhy08'],[0.000000,-1.000000,0.000000],[0.000000,0.000000,20.000000],[290.147675,-796.901123,9.138309],[1.000000,1.000000,20.000000]]),
        'flaser' : ([['beachball'],[2.313936,-7.656188,-0.168825],[0.595772,0.004145,7.977784],[280.124542,-796.915894,3.600792],[8,8,8]],
                [['marblephy06'],[-2.182297,-9.758976,0.000000],[0.000000,0.000000,0.100000],[279.913605,-796.871521,15.405395],[10,10,.1]],
                [['marblephy07'],[-1.091148,-4.879488,0.000000],[0.000000,0.000000,0.100000],[279.913605,-796.871521,17.405396],[5,5,.1]],
                [['marblephy08'],[-1.091148,-4.879488,0.000000],[0.000000,0.000000,0.100000],[279.913605,-796.871521,19.405396],[5,5,.1]],
                [['orangecone01'],[6.823526,4.176061,0.000000],[0.000000,0.000000,10.000000],[280.282623,-796.483582,8.678108],[8,8,10]],
                [['orangecone04'],[-0.012956,-0.556473,0.830765],[-0.999577,0.028856,0.003741],[269.727844,-796.932495,9.409465],[1,1,1]],
                [['orangecone05'],[0.045567,0.586891,-0.808383],[0.997495,-0.070556,0.005003],[290.790192,-796.814636,9.358028],[1,1,1]]),
        # Son of PumpkinMan  04-09-2005
        'pumpkinson' : ([['pumpkin01'],[0.000000,-0.433013,-0.250000],[0.000000,-0.250000,0.433013],[242.517059,-816.612183,6.608408],[0.5,0.5,0.5]],
                [['OrangeCone11'],[0.000000,0.125000,0.000000],[-0.003500,0.000000,-0.624755],[242.174744,-816.414856,3.483639],[0.125,0.125,0.625]],
                [['OrangeCone01'],[0.456126,0.204807,0.001789],[0.052056,-0.120149,0.482550],[242.709961,-816.837341,7.483221],[0.5,0.5,0.5]],
                [['beachball'],[0.000085,0.124099,0.014978],[-0.000472,0.014979,-0.124096],[242.500244,-816.847046,6.108267],[0.0625,0.125,0.125]],
                [['MarblePhy06'],[0.000000,-0.125000,0.000000],[0.000000,0.000000,0.125000],[242.708206,-817.178650,6.233492],[0.125,0.125,0.125]],
                [['MarblePhy07'],[0.000000,-0.125000,0.000000],[0.000000,0.000000,0.125000],[242.220718,-817.141174,6.233496],[0.125,0.125,0.125]],
                [['OrangeCone17'],[0.000000,-0.125000,0.000000],[0.000000,0.000000,1.250000],[242.549744,-816.414856,4.858639],[0.125,0.125,1.25]],
                [['OrangeCone04'],[0.000000,0.500000,0.000000],[0.000000,0.000000,-0.500000],[242.558365,-816.382690,3.984400],[0.5,0.5,0.5]],
                [['OrangeCone05'],[0.000000,0.125000,0.000000],[0.003500,0.000000,-0.624755],[242.924744,-816.414856,3.483639],[0.125,0.125,0.625]],
                [['OrangeCone12'],[-0.492404,-0.086824,0.000000],[0.000000,0.000000,0.500000],[242.549744,-816.414917,5.233637],[0.5,0.5,0.5]],
                [['OrangeCone15'],[0.000000,-0.125000,0.000000],[0.625000,0.000000,0.000000],[242.924744,-816.414856,5.483637],[0.625,0.125,0.125]],
                [['OrangeCone16'],[0.000000,-0.125000,0.000000],[-0.625000,0.000000,0.000000],[242.174744,-816.414856,5.483637],[0.625,0.125,0.125]]),
        #Makes a ballroom around the fountain for dancing
        'ballroom' : ([['beachball'],[29.999920,0.068797,0.000000],[-0.068797,29.999924,-0.000000],[279.689911,-796.553650,2.485018],[30,30,0.1]],
                [['orangecone01'],[0.000000,-80.000000,0.000000],[0.000000,0.000000,400.000000],[280.011627,-796.978210,3.537237],[80,80,400]],
                [['MarblePhy06'],[0.000000,-5.000000,0.000000],[0.000000,0.000000,5.000000],[278.719879,-801.720947,32.607315],[5,5,5]],
                [['MarblePhy07'],[0.000000,-5.000000,0.000000],[0.000000,0.000000,5.000000],[282.949921,-800.755432,32.607315],[5,5,5]],
                [['MarblePhy08'],[0.000000,-5.000000,0.000000],[0.000000,0.000000,5.000000],[284.832428,-796.846252,32.607315],[5,5,5]],
                [['pumpkin01'],[-0.731671,10.975640,-0.000001],[0.000000,-0.000001,-11.000000],[279.872284,-797.204590,-3.401621],[11,11,11]],
                [['pumpkin02'],[-0.311034,-0.950399,0.000000],[0.000000,0.000000,1.000000],[279.671783,-797.601501,10.604023]]),
    }
}
# end of StructLists

# begin of AnimLists
AnimLists = {
    # The Evil Zombi Face "Works best on male figure"
    'zombi' : (['FemaleFall2','FemaleFall2','FemaleFall2','FemaleFall2','FemaleFall2'],
               ['FemaleFall2','FemaleFall2','FemaleFall2','FemaleFall2','FemaleFall2']),
    # The full ladder climbing animation. The middle part can be extended for higher "ladders"
    'ladderup' : (['MaleLadderUpOn','MaleLadderUp','MaleLadderUp','MaleLadderUp','MaleLadderUpOff'],
                  ['FemaleLadderUpOn','FemaleLadderUp','FemaleLadderUp','FemaleLadderUp','FemaleLadderUpOff']),
    # The full ladder descending animation. The middle part can be extended for higher "ladders"
    'ladderdown' : (['MaleLadderDownOn','MaleLadderDown','MaleLadderDown','MaleLadderDown','MaleLadderDownOff'],
                    ['FemaleLadderDownOn','FemaleLadderDown','FemaleLadderDown','FemaleLadderDown','FemaleLadderDownOff']),
    # A longer swim sequence
    'swimfast' : (['MaleSwimFast','MaleSwimFast','MaleSwimFast','MaleSwimFast','MaleSwimFast'],
                  ['FemaleSwimFast','FemaleSwimFast','FemaleSwimFast','FemaleSwimFast','FemaleSwimFast']),
    # Another longer swim sequence
    'swimslow' : (['MaleSwimSlow','MaleSwimSlow','MaleSwimSlow','MaleSwimSlow','MaleSwimSlow'],
                  ['FemaleSwimSlow','FemaleSwimSlow','FemaleSwimSlow','FemaleSwimSlow','FemaleSwimSlow']),
    # The full sit down and stand up animation. The middle part can be extended for longer sits
    'sitstand' : (['MaleSitDown','MaleSitIdle','MaleSitIdle','MaleSitIdle','MaleSitIdle','MaleSitStand'],
                  ['FemaleSitDown','FemaleSitIdle','FemaleSitIdle','FemaleSitIdle','FemaleSitIdle','FemaleSitStand']),
    # a longer dance
    'dance' : (['MaleDance','MaleDance'],['FemaleDance','FemaleDance']),
    # longer dance that makes males do the female dance and vice versa
    'trandance' : (['FemaleDance','FemaleDance'],['MaleDance','MaleDance']),
    # "Use" any object (I know it looks long, but the ScopeHold anims are actually really short...)
    'hold' : (['MaleGlobalScopeGrab','MaleGlobalScopeHold','MaleGlobalScopeHold',
            'MaleGlobalScopeHold','MaleGlobalScopeHold','MaleGlobalScopeHold',
            'MaleGlobalScopeHold','MaleGlobalScopeHold','MaleGlobalScopeHold',
            'MaleGlobalScopeHold','MaleGlobalScopeHold','MaleGlobalScopeHold',
            'MaleGlobalScopeHold','MaleGlobalScopeHold','MaleGlobalScopeHold',
            'MaleGlobalScopeHold','MaleGlobalScopeHold','MaleGlobalScopeHold',
            'MaleGlobalScopeHold','MaleGlobalScopeHold','MaleGlobalScopeHold',
            'MaleGlobalScopeRelease'],
        ['FemaleGlobalScopeGrab','FemaleGlobalScopeHold',
            'FemaleGlobalScopeHold','FemaleGlobalScopeHold','FemaleGlobalScopeHold',
            'FemaleGlobalScopeHold','FemaleGlobalScopeHold','FemaleGlobalScopeHold',
            'FemaleGlobalScopeHold','FemaleGlobalScopeHold','FemaleGlobalScopeHold',
            'FemaleGlobalScopeHold','FemaleGlobalScopeHold','FemaleGlobalScopeHold',
            'FemaleGlobalScopeHold','FemaleGlobalScopeHold','FemaleGlobalScopeHold',
            'FemaleGlobalScopeHold','FemaleGlobalScopeHold','FemaleGlobalScopeHold',
            'FemaleGlobalScopeHold','FemaleGlobalScopeRelease']),
}
# end of AnimLists
