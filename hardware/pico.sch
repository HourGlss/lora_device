EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Switch:SW_MEC_5E SW1
U 1 1 61B9A0DB
P 4400 4400
F 0 "SW1" H 4400 4785 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 4694 50  0000 C CNN
F 2 "" H 4400 4700 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 4700 50  0001 C CNN
	1    4400 4400
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D1
U 1 1 61BA1516
P 4050 4300
F 0 "D1" H 4050 4517 50  0000 C CNN
F 1 "1N4148" H 4050 4426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 4125 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 4300 50  0001 C CNN
	1    4050 4300
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW2
U 1 1 61BAB456
P 4400 4600
F 0 "SW2" H 4400 4985 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 4894 50  0000 C CNN
F 2 "" H 4400 4900 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 4900 50  0001 C CNN
	1    4400 4600
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D2
U 1 1 61BAB45C
P 4050 4500
F 0 "D2" H 4050 4717 50  0000 C CNN
F 1 "1N4148" H 4050 4626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 4325 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 4500 50  0001 C CNN
	1    4050 4500
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 4300 4750 4300
$Comp
L REYAX_RYLR896:REYAX_RYLR896 IC1
U 1 1 61BC33C7
P 8100 1800
F 0 "IC1" V 8488 1172 50  0000 R CNN
F 1 "REYAX_RYLR896" V 8397 1172 50  0000 R CNN
F 2 "REYAXRYLR896" H 8850 1900 50  0001 L CNN
F 3 "http://reyax.com/products/rylr896/" H 8850 1800 50  0001 L CNN
F 4 "RYLR896 transceiver module" H 8850 1700 50  0001 L CNN "Description"
F 5 "25" H 8850 1600 50  0001 L CNN "Height"
F 6 "Reyax" H 8850 1500 50  0001 L CNN "Manufacturer_Name"
F 7 "REYAX RYLR896" H 8850 1400 50  0001 L CNN "Manufacturer_Part_Number"
F 8 "" H 8850 1300 50  0001 L CNN "Mouser Part Number"
F 9 "" H 8850 1200 50  0001 L CNN "Mouser Price/Stock"
F 10 "" H 8850 1100 50  0001 L CNN "Arrow Part Number"
F 11 "" H 8850 1000 50  0001 L CNN "Arrow Price/Stock"
	1    8100 1800
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4750 4500 4750 4300
Wire Wire Line
	4600 4500 4750 4500
$Comp
L Switch:SW_MEC_5E SW3
U 1 1 61BE5F86
P 4400 4800
F 0 "SW3" H 4400 5185 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 5094 50  0000 C CNN
F 2 "" H 4400 5100 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 5100 50  0001 C CNN
	1    4400 4800
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D3
U 1 1 61BE5F8C
P 4050 4700
F 0 "D3" H 4050 4917 50  0000 C CNN
F 1 "1N4148" H 4050 4826 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 4525 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 4700 50  0001 C CNN
	1    4050 4700
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW4
U 1 1 61BE5F92
P 4400 5000
F 0 "SW4" H 4400 5385 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 5294 50  0000 C CNN
F 2 "" H 4400 5300 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 5300 50  0001 C CNN
	1    4400 5000
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D4
U 1 1 61BE5F98
P 4050 4900
F 0 "D4" H 4050 5117 50  0000 C CNN
F 1 "1N4148" H 4050 5026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 4725 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 4900 50  0001 C CNN
	1    4050 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 4700 4750 4700
Wire Wire Line
	4750 4900 4750 4700
Wire Wire Line
	4600 4900 4750 4900
Wire Wire Line
	4750 4500 4750 4700
Connection ~ 4750 4500
Connection ~ 4750 4700
$Comp
L Switch:SW_MEC_5E SW5
U 1 1 61BF02E2
P 4400 5200
F 0 "SW5" H 4400 5585 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 5494 50  0000 C CNN
F 2 "" H 4400 5500 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 5500 50  0001 C CNN
	1    4400 5200
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D5
U 1 1 61BF02E8
P 4050 5100
F 0 "D5" H 4050 5317 50  0000 C CNN
F 1 "1N4148" H 4050 5226 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 4925 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 5100 50  0001 C CNN
	1    4050 5100
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW6
U 1 1 61BF02EE
P 4400 5400
F 0 "SW6" H 4400 5785 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 5694 50  0000 C CNN
F 2 "" H 4400 5700 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 5700 50  0001 C CNN
	1    4400 5400
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D6
U 1 1 61BF02F4
P 4050 5300
F 0 "D6" H 4050 5517 50  0000 C CNN
F 1 "1N4148" H 4050 5426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 5125 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 5300 50  0001 C CNN
	1    4050 5300
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 5100 4750 5100
Wire Wire Line
	4750 5300 4750 5100
Wire Wire Line
	4600 5300 4750 5300
$Comp
L Switch:SW_MEC_5E SW7
U 1 1 61BF02FD
P 4400 5600
F 0 "SW7" H 4400 5985 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 5894 50  0000 C CNN
F 2 "" H 4400 5900 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 5900 50  0001 C CNN
	1    4400 5600
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D7
U 1 1 61BF0303
P 4050 5500
F 0 "D7" H 4050 5717 50  0000 C CNN
F 1 "1N4148" H 4050 5626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 5325 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 5500 50  0001 C CNN
	1    4050 5500
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW8
U 1 1 61BF0309
P 4400 5800
F 0 "SW8" H 4400 6185 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 6094 50  0000 C CNN
F 2 "" H 4400 6100 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 6100 50  0001 C CNN
	1    4400 5800
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D8
U 1 1 61BF030F
P 4050 5700
F 0 "D8" H 4050 5917 50  0000 C CNN
F 1 "1N4148" H 4050 5826 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 5525 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 5700 50  0001 C CNN
	1    4050 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 5500 4750 5500
Wire Wire Line
	4750 5700 4750 5500
Wire Wire Line
	4600 5700 4750 5700
Wire Wire Line
	4750 5300 4750 5500
Connection ~ 4750 5300
Connection ~ 4750 5500
Wire Wire Line
	4750 4900 4750 5100
Connection ~ 4750 4900
Connection ~ 4750 5100
$Comp
L Switch:SW_MEC_5E SW9
U 1 1 61BF729F
P 4400 6000
F 0 "SW9" H 4400 6385 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 6294 50  0000 C CNN
F 2 "" H 4400 6300 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 6300 50  0001 C CNN
	1    4400 6000
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW10
U 1 1 61BF72A5
P 4400 6200
F 0 "SW10" H 4400 6585 50  0000 C CNN
F 1 "SW_MEC_5E" H 4400 6494 50  0000 C CNN
F 2 "" H 4400 6500 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 4400 6500 50  0001 C CNN
	1    4400 6200
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D10
U 1 1 61BF72AB
P 4050 6100
F 0 "D10" H 4050 6317 50  0000 C CNN
F 1 "1N4148" H 4050 6226 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 5925 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 6100 50  0001 C CNN
	1    4050 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	4600 6100 4750 6100
$Comp
L Diode:1N4148 D9
U 1 1 61BF89E3
P 4050 5900
F 0 "D9" H 4050 6117 50  0000 C CNN
F 1 "1N4148" H 4050 6026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 4050 5725 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 4050 5900 50  0001 C CNN
	1    4050 5900
	1    0    0    -1  
$EndComp
Wire Wire Line
	4750 5700 4750 5900
Connection ~ 4750 5700
Wire Wire Line
	4600 5900 4750 5900
Connection ~ 4750 5900
Wire Wire Line
	4750 5900 4750 6100
$Comp
L Switch:SW_MEC_5E SW11
U 1 1 61C10415
P 5450 4400
F 0 "SW11" H 5450 4785 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 4694 50  0000 C CNN
F 2 "" H 5450 4700 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 4700 50  0001 C CNN
	1    5450 4400
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D11
U 1 1 61C1041B
P 5100 4300
F 0 "D11" H 5100 4517 50  0000 C CNN
F 1 "1N4148" H 5100 4426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 4125 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 4300 50  0001 C CNN
	1    5100 4300
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW12
U 1 1 61C10421
P 5450 4600
F 0 "SW12" H 5450 4985 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 4894 50  0000 C CNN
F 2 "" H 5450 4900 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 4900 50  0001 C CNN
	1    5450 4600
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D12
U 1 1 61C10427
P 5100 4500
F 0 "D12" H 5100 4717 50  0000 C CNN
F 1 "1N4148" H 5100 4626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 4325 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 4500 50  0001 C CNN
	1    5100 4500
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 4300 5800 4300
Wire Wire Line
	5800 4500 5800 4300
Wire Wire Line
	5650 4500 5800 4500
$Comp
L Switch:SW_MEC_5E SW13
U 1 1 61C10430
P 5450 4800
F 0 "SW13" H 5450 5185 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 5094 50  0000 C CNN
F 2 "" H 5450 5100 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 5100 50  0001 C CNN
	1    5450 4800
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D13
U 1 1 61C10436
P 5100 4700
F 0 "D13" H 5100 4917 50  0000 C CNN
F 1 "1N4148" H 5100 4826 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 4525 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 4700 50  0001 C CNN
	1    5100 4700
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW14
U 1 1 61C1043C
P 5450 5000
F 0 "SW14" H 5450 5385 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 5294 50  0000 C CNN
F 2 "" H 5450 5300 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 5300 50  0001 C CNN
	1    5450 5000
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D14
U 1 1 61C10442
P 5100 4900
F 0 "D14" H 5100 5117 50  0000 C CNN
F 1 "1N4148" H 5100 5026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 4725 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 4900 50  0001 C CNN
	1    5100 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 4700 5800 4700
Wire Wire Line
	5800 4900 5800 4700
Wire Wire Line
	5650 4900 5800 4900
Wire Wire Line
	5800 4500 5800 4700
Connection ~ 5800 4500
Connection ~ 5800 4700
$Comp
L Switch:SW_MEC_5E SW15
U 1 1 61C1044E
P 5450 5200
F 0 "SW15" H 5450 5585 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 5494 50  0000 C CNN
F 2 "" H 5450 5500 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 5500 50  0001 C CNN
	1    5450 5200
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D15
U 1 1 61C10454
P 5100 5100
F 0 "D15" H 5100 5317 50  0000 C CNN
F 1 "1N4148" H 5100 5226 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 4925 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 5100 50  0001 C CNN
	1    5100 5100
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW16
U 1 1 61C1045A
P 5450 5400
F 0 "SW16" H 5450 5785 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 5694 50  0000 C CNN
F 2 "" H 5450 5700 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 5700 50  0001 C CNN
	1    5450 5400
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D16
U 1 1 61C10460
P 5100 5300
F 0 "D16" H 5100 5517 50  0000 C CNN
F 1 "1N4148" H 5100 5426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 5125 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 5300 50  0001 C CNN
	1    5100 5300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 5100 5800 5100
Wire Wire Line
	5800 5300 5800 5100
Wire Wire Line
	5650 5300 5800 5300
$Comp
L Switch:SW_MEC_5E SW17
U 1 1 61C10469
P 5450 5600
F 0 "SW17" H 5450 5985 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 5894 50  0000 C CNN
F 2 "" H 5450 5900 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 5900 50  0001 C CNN
	1    5450 5600
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D17
U 1 1 61C1046F
P 5100 5500
F 0 "D17" H 5100 5717 50  0000 C CNN
F 1 "1N4148" H 5100 5626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 5325 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 5500 50  0001 C CNN
	1    5100 5500
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW18
U 1 1 61C10475
P 5450 5800
F 0 "SW18" H 5450 6185 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 6094 50  0000 C CNN
F 2 "" H 5450 6100 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 6100 50  0001 C CNN
	1    5450 5800
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D18
U 1 1 61C1047B
P 5100 5700
F 0 "D18" H 5100 5917 50  0000 C CNN
F 1 "1N4148" H 5100 5826 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 5525 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 5700 50  0001 C CNN
	1    5100 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 5500 5800 5500
Wire Wire Line
	5800 5700 5800 5500
Wire Wire Line
	5650 5700 5800 5700
Wire Wire Line
	5800 5300 5800 5500
Connection ~ 5800 5300
Connection ~ 5800 5500
Wire Wire Line
	5800 4900 5800 5100
Connection ~ 5800 4900
Connection ~ 5800 5100
$Comp
L Switch:SW_MEC_5E SW19
U 1 1 61C1048A
P 5450 6000
F 0 "SW19" H 5450 6385 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 6294 50  0000 C CNN
F 2 "" H 5450 6300 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 6300 50  0001 C CNN
	1    5450 6000
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW20
U 1 1 61C10490
P 5450 6200
F 0 "SW20" H 5450 6585 50  0000 C CNN
F 1 "SW_MEC_5E" H 5450 6494 50  0000 C CNN
F 2 "" H 5450 6500 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 5450 6500 50  0001 C CNN
	1    5450 6200
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D20
U 1 1 61C10496
P 5100 6100
F 0 "D20" H 5100 6317 50  0000 C CNN
F 1 "1N4148" H 5100 6226 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 5925 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 6100 50  0001 C CNN
	1    5100 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 6100 5800 6100
$Comp
L Diode:1N4148 D19
U 1 1 61C104AC
P 5100 5900
F 0 "D19" H 5100 6117 50  0000 C CNN
F 1 "1N4148" H 5100 6026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 5100 5725 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 5100 5900 50  0001 C CNN
	1    5100 5900
	1    0    0    -1  
$EndComp
Wire Wire Line
	5800 5700 5800 5900
Connection ~ 5800 5700
Wire Wire Line
	5650 5900 5800 5900
Connection ~ 5800 5900
Wire Wire Line
	5800 5900 5800 6100
$Comp
L Switch:SW_MEC_5E SW21
U 1 1 61C1664E
P 6450 4400
F 0 "SW21" H 6450 4785 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 4694 50  0000 C CNN
F 2 "" H 6450 4700 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 4700 50  0001 C CNN
	1    6450 4400
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D21
U 1 1 61C16654
P 6100 4300
F 0 "D21" H 6100 4517 50  0000 C CNN
F 1 "1N4148" H 6100 4426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 4125 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 4300 50  0001 C CNN
	1    6100 4300
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW22
U 1 1 61C1665A
P 6450 4600
F 0 "SW22" H 6450 4985 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 4894 50  0000 C CNN
F 2 "" H 6450 4900 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 4900 50  0001 C CNN
	1    6450 4600
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D22
U 1 1 61C16660
P 6100 4500
F 0 "D22" H 6100 4717 50  0000 C CNN
F 1 "1N4148" H 6100 4626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 4325 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 4500 50  0001 C CNN
	1    6100 4500
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 4300 6800 4300
Wire Wire Line
	6800 4500 6800 4300
Wire Wire Line
	6650 4500 6800 4500
$Comp
L Switch:SW_MEC_5E SW23
U 1 1 61C16669
P 6450 4800
F 0 "SW23" H 6450 5185 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 5094 50  0000 C CNN
F 2 "" H 6450 5100 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 5100 50  0001 C CNN
	1    6450 4800
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D23
U 1 1 61C1666F
P 6100 4700
F 0 "D23" H 6100 4917 50  0000 C CNN
F 1 "1N4148" H 6100 4826 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 4525 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 4700 50  0001 C CNN
	1    6100 4700
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW24
U 1 1 61C16675
P 6450 5000
F 0 "SW24" H 6450 5385 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 5294 50  0000 C CNN
F 2 "" H 6450 5300 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 5300 50  0001 C CNN
	1    6450 5000
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D24
U 1 1 61C1667B
P 6100 4900
F 0 "D24" H 6100 5117 50  0000 C CNN
F 1 "1N4148" H 6100 5026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 4725 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 4900 50  0001 C CNN
	1    6100 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 4700 6800 4700
Wire Wire Line
	6800 4900 6800 4700
Wire Wire Line
	6650 4900 6800 4900
Wire Wire Line
	6800 4500 6800 4700
Connection ~ 6800 4500
Connection ~ 6800 4700
$Comp
L Switch:SW_MEC_5E SW25
U 1 1 61C16687
P 6450 5200
F 0 "SW25" H 6450 5585 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 5494 50  0000 C CNN
F 2 "" H 6450 5500 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 5500 50  0001 C CNN
	1    6450 5200
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D25
U 1 1 61C1668D
P 6100 5100
F 0 "D25" H 6100 5317 50  0000 C CNN
F 1 "1N4148" H 6100 5226 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 4925 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 5100 50  0001 C CNN
	1    6100 5100
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW26
U 1 1 61C16693
P 6450 5400
F 0 "SW26" H 6450 5785 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 5694 50  0000 C CNN
F 2 "" H 6450 5700 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 5700 50  0001 C CNN
	1    6450 5400
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D26
U 1 1 61C16699
P 6100 5300
F 0 "D26" H 6100 5517 50  0000 C CNN
F 1 "1N4148" H 6100 5426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 5125 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 5300 50  0001 C CNN
	1    6100 5300
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 5100 6800 5100
Wire Wire Line
	6800 5300 6800 5100
Wire Wire Line
	6650 5300 6800 5300
$Comp
L Switch:SW_MEC_5E SW27
U 1 1 61C166A2
P 6450 5600
F 0 "SW27" H 6450 5985 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 5894 50  0000 C CNN
F 2 "" H 6450 5900 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 5900 50  0001 C CNN
	1    6450 5600
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D27
U 1 1 61C166A8
P 6100 5500
F 0 "D27" H 6100 5717 50  0000 C CNN
F 1 "1N4148" H 6100 5626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 5325 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 5500 50  0001 C CNN
	1    6100 5500
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW28
U 1 1 61C166AE
P 6450 5800
F 0 "SW28" H 6450 6185 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 6094 50  0000 C CNN
F 2 "" H 6450 6100 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 6100 50  0001 C CNN
	1    6450 5800
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D28
U 1 1 61C166B4
P 6100 5700
F 0 "D28" H 6100 5917 50  0000 C CNN
F 1 "1N4148" H 6100 5826 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 5525 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 5700 50  0001 C CNN
	1    6100 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 5500 6800 5500
Wire Wire Line
	6800 5700 6800 5500
Wire Wire Line
	6650 5700 6800 5700
Wire Wire Line
	6800 5300 6800 5500
Connection ~ 6800 5300
Connection ~ 6800 5500
Wire Wire Line
	6800 4900 6800 5100
Connection ~ 6800 4900
Connection ~ 6800 5100
$Comp
L Switch:SW_MEC_5E SW29
U 1 1 61C166C3
P 6450 6000
F 0 "SW29" H 6450 6385 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 6294 50  0000 C CNN
F 2 "" H 6450 6300 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 6300 50  0001 C CNN
	1    6450 6000
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW30
U 1 1 61C166C9
P 6450 6200
F 0 "SW30" H 6450 6585 50  0000 C CNN
F 1 "SW_MEC_5E" H 6450 6494 50  0000 C CNN
F 2 "" H 6450 6500 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 6450 6500 50  0001 C CNN
	1    6450 6200
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D30
U 1 1 61C166CF
P 6100 6100
F 0 "D30" H 6100 6317 50  0000 C CNN
F 1 "1N4148" H 6100 6226 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 5925 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 6100 50  0001 C CNN
	1    6100 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 6100 6800 6100
$Comp
L Diode:1N4148 D29
U 1 1 61C166E5
P 6100 5900
F 0 "D29" H 6100 6117 50  0000 C CNN
F 1 "1N4148" H 6100 6026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 6100 5725 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 6100 5900 50  0001 C CNN
	1    6100 5900
	1    0    0    -1  
$EndComp
Wire Wire Line
	6800 5700 6800 5900
Connection ~ 6800 5700
Wire Wire Line
	6650 5900 6800 5900
Connection ~ 6800 5900
Wire Wire Line
	6800 5900 6800 6100
$Comp
L Switch:SW_MEC_5E SW31
U 1 1 61C1E915
P 7550 4400
F 0 "SW31" H 7550 4785 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 4694 50  0000 C CNN
F 2 "" H 7550 4700 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 4700 50  0001 C CNN
	1    7550 4400
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D32
U 1 1 61C1E91B
P 7200 4300
F 0 "D32" H 7200 4517 50  0000 C CNN
F 1 "1N4148" H 7200 4426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 4125 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 4300 50  0001 C CNN
	1    7200 4300
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW32
U 1 1 61C1E921
P 7550 4600
F 0 "SW32" H 7550 4985 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 4894 50  0000 C CNN
F 2 "" H 7550 4900 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 4900 50  0001 C CNN
	1    7550 4600
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D33
U 1 1 61C1E927
P 7200 4500
F 0 "D33" H 7200 4717 50  0000 C CNN
F 1 "1N4148" H 7200 4626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 4325 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 4500 50  0001 C CNN
	1    7200 4500
	1    0    0    -1  
$EndComp
Wire Wire Line
	7750 4300 7900 4300
Wire Wire Line
	7900 4500 7900 4300
Wire Wire Line
	7750 4500 7900 4500
$Comp
L Switch:SW_MEC_5E SW33
U 1 1 61C1E930
P 7550 4800
F 0 "SW33" H 7550 5185 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 5094 50  0000 C CNN
F 2 "" H 7550 5100 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 5100 50  0001 C CNN
	1    7550 4800
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D34
U 1 1 61C1E936
P 7200 4700
F 0 "D34" H 7200 4917 50  0000 C CNN
F 1 "1N4148" H 7200 4826 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 4525 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 4700 50  0001 C CNN
	1    7200 4700
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW34
U 1 1 61C1E93C
P 7550 5000
F 0 "SW34" H 7550 5385 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 5294 50  0000 C CNN
F 2 "" H 7550 5300 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 5300 50  0001 C CNN
	1    7550 5000
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D35
U 1 1 61C1E942
P 7200 4900
F 0 "D35" H 7200 5117 50  0000 C CNN
F 1 "1N4148" H 7200 5026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 4725 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 4900 50  0001 C CNN
	1    7200 4900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7750 4700 7900 4700
Wire Wire Line
	7900 4900 7900 4700
Wire Wire Line
	7750 4900 7900 4900
Wire Wire Line
	7900 4500 7900 4700
Connection ~ 7900 4500
Connection ~ 7900 4700
$Comp
L Switch:SW_MEC_5E SW35
U 1 1 61C1E94E
P 7550 5200
F 0 "SW35" H 7550 5585 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 5494 50  0000 C CNN
F 2 "" H 7550 5500 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 5500 50  0001 C CNN
	1    7550 5200
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D36
U 1 1 61C1E954
P 7200 5100
F 0 "D36" H 7200 5317 50  0000 C CNN
F 1 "1N4148" H 7200 5226 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 4925 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 5100 50  0001 C CNN
	1    7200 5100
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW36
U 1 1 61C1E95A
P 7550 5400
F 0 "SW36" H 7550 5785 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 5694 50  0000 C CNN
F 2 "" H 7550 5700 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 5700 50  0001 C CNN
	1    7550 5400
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D37
U 1 1 61C1E960
P 7200 5300
F 0 "D37" H 7200 5517 50  0000 C CNN
F 1 "1N4148" H 7200 5426 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 5125 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 5300 50  0001 C CNN
	1    7200 5300
	1    0    0    -1  
$EndComp
Wire Wire Line
	7750 5100 7900 5100
Wire Wire Line
	7900 5300 7900 5100
Wire Wire Line
	7750 5300 7900 5300
$Comp
L Switch:SW_MEC_5E SW37
U 1 1 61C1E969
P 7550 5600
F 0 "SW37" H 7550 5985 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 5894 50  0000 C CNN
F 2 "" H 7550 5900 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 5900 50  0001 C CNN
	1    7550 5600
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D38
U 1 1 61C1E96F
P 7200 5500
F 0 "D38" H 7200 5717 50  0000 C CNN
F 1 "1N4148" H 7200 5626 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 5325 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 5500 50  0001 C CNN
	1    7200 5500
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW38
U 1 1 61C1E975
P 7550 5800
F 0 "SW38" H 7550 6185 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 6094 50  0000 C CNN
F 2 "" H 7550 6100 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 6100 50  0001 C CNN
	1    7550 5800
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D39
U 1 1 61C1E97B
P 7200 5700
F 0 "D39" H 7200 5917 50  0000 C CNN
F 1 "1N4148" H 7200 5826 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 5525 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 5700 50  0001 C CNN
	1    7200 5700
	1    0    0    -1  
$EndComp
Wire Wire Line
	7750 5500 7900 5500
Wire Wire Line
	7900 5700 7900 5500
Wire Wire Line
	7750 5700 7900 5700
Wire Wire Line
	7900 5300 7900 5500
Connection ~ 7900 5300
Connection ~ 7900 5500
Wire Wire Line
	7900 4900 7900 5100
Connection ~ 7900 4900
Connection ~ 7900 5100
$Comp
L Switch:SW_MEC_5E SW39
U 1 1 61C1E98A
P 7550 6000
F 0 "SW39" H 7550 6385 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 6294 50  0000 C CNN
F 2 "" H 7550 6300 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 6300 50  0001 C CNN
	1    7550 6000
	1    0    0    -1  
$EndComp
$Comp
L Switch:SW_MEC_5E SW40
U 1 1 61C1E990
P 7550 6200
F 0 "SW40" H 7550 6585 50  0000 C CNN
F 1 "SW_MEC_5E" H 7550 6494 50  0000 C CNN
F 2 "" H 7550 6500 50  0001 C CNN
F 3 "http://www.apem.com/int/index.php?controller=attachment&id_attachment=1371" H 7550 6500 50  0001 C CNN
	1    7550 6200
	1    0    0    -1  
$EndComp
$Comp
L Diode:1N4148 D41
U 1 1 61C1E996
P 7200 6100
F 0 "D41" H 7200 6317 50  0000 C CNN
F 1 "1N4148" H 7200 6226 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 5925 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 6100 50  0001 C CNN
	1    7200 6100
	1    0    0    -1  
$EndComp
Wire Wire Line
	7750 6100 7900 6100
$Comp
L Diode:1N4148 D40
U 1 1 61C1E9AC
P 7200 5900
F 0 "D40" H 7200 6117 50  0000 C CNN
F 1 "1N4148" H 7200 6026 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 7200 5725 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/1N4148_1N4448.pdf" H 7200 5900 50  0001 C CNN
	1    7200 5900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7900 5700 7900 5900
Connection ~ 7900 5700
Wire Wire Line
	7750 5900 7900 5900
Connection ~ 7900 5900
Wire Wire Line
	7900 5900 7900 6100
Wire Wire Line
	8100 2100 8100 1800
Wire Wire Line
	8400 3500 8400 1800
Wire Wire Line
	5300 3600 5300 3800
Wire Wire Line
	5300 3800 5900 3800
Wire Wire Line
	7900 3800 7900 4300
Connection ~ 7900 4300
Wire Wire Line
	6800 4300 6800 3850
Wire Wire Line
	6800 3850 5250 3850
Wire Wire Line
	5250 3850 5250 3500
Wire Wire Line
	5250 3500 5300 3500
Connection ~ 6800 4300
Wire Wire Line
	5800 4300 5800 3900
Wire Wire Line
	5800 3900 5200 3900
Wire Wire Line
	5200 3900 5200 3300
Wire Wire Line
	5200 3300 5300 3300
Connection ~ 5800 4300
Wire Wire Line
	4750 4300 4750 3200
Wire Wire Line
	4750 3200 5300 3200
Connection ~ 4750 4300
Wire Wire Line
	3800 4300 3800 3100
Wire Wire Line
	3900 4300 3800 4300
Wire Wire Line
	3900 4500 3700 4500
Wire Wire Line
	3700 3000 3700 4500
Wire Wire Line
	3600 4700 3900 4700
Wire Wire Line
	3600 2800 3600 4700
Wire Wire Line
	3500 4900 3900 4900
Wire Wire Line
	3900 5100 3400 5100
Wire Wire Line
	3300 5300 3900 5300
Wire Wire Line
	3900 5500 3150 5500
Wire Wire Line
	3050 5700 3900 5700
Wire Wire Line
	3900 5900 2950 5900
Wire Wire Line
	2850 6100 3900 6100
Wire Wire Line
	4950 4300 4900 4300
Wire Wire Line
	4950 4500 4900 4500
Wire Wire Line
	4950 4700 4900 4700
Wire Wire Line
	4950 4900 4900 4900
Wire Wire Line
	4950 5100 4900 5100
Wire Wire Line
	4950 5300 4900 5300
Wire Wire Line
	4950 5500 4900 5500
Wire Wire Line
	4950 5700 4900 5700
Wire Wire Line
	4950 5900 4900 5900
Wire Wire Line
	4950 6100 4900 6100
Wire Wire Line
	4850 5900 4850 5850
Wire Wire Line
	4850 5850 3900 5850
Wire Wire Line
	3900 5850 3900 5900
Connection ~ 3900 5900
Wire Wire Line
	4850 6100 4850 6050
Wire Wire Line
	4850 6050 3900 6050
Wire Wire Line
	3900 6050 3900 6100
Connection ~ 3900 6100
Wire Wire Line
	4850 5700 4850 5650
Wire Wire Line
	4850 5650 3900 5650
Wire Wire Line
	3900 5650 3900 5700
Connection ~ 3900 5700
Wire Wire Line
	4850 5500 4850 5450
Wire Wire Line
	3900 5450 4850 5450
Wire Wire Line
	3900 5450 3900 5500
Connection ~ 3900 5500
Wire Wire Line
	4850 5300 4850 5250
Wire Wire Line
	4850 5250 3900 5250
Wire Wire Line
	3900 5250 3900 5300
Connection ~ 3900 5300
Wire Wire Line
	3900 5100 3900 5050
Connection ~ 3900 5100
Wire Wire Line
	3900 5050 4850 5050
Wire Wire Line
	4850 5050 4850 5100
Wire Wire Line
	4850 4900 4850 4850
Wire Wire Line
	4850 4850 3900 4850
Wire Wire Line
	3900 4900 3900 4850
Connection ~ 3900 4900
Wire Wire Line
	3900 4700 3900 4650
Connection ~ 3900 4700
Wire Wire Line
	3900 4650 4850 4650
Wire Wire Line
	4850 4650 4850 4700
Wire Wire Line
	4850 4500 4850 4450
Wire Wire Line
	4850 4450 3900 4450
Wire Wire Line
	3900 4450 3900 4500
Connection ~ 3900 4500
Wire Wire Line
	3900 4300 3900 4250
Connection ~ 3900 4300
Wire Wire Line
	3900 4250 4850 4250
Wire Wire Line
	4850 4250 4850 4300
Wire Wire Line
	5950 4500 5850 4500
Wire Wire Line
	5950 4700 5850 4700
Wire Wire Line
	5950 4900 5850 4900
Wire Wire Line
	5950 5100 5850 5100
Wire Wire Line
	5950 5300 5850 5300
Wire Wire Line
	5950 5500 5850 5500
Wire Wire Line
	5950 5700 5850 5700
Wire Wire Line
	5950 5900 5850 5900
Wire Wire Line
	5950 6100 5850 6100
Wire Wire Line
	5850 5900 5850 5850
Wire Wire Line
	5850 5850 4900 5850
Wire Wire Line
	5850 6100 5850 6050
Wire Wire Line
	5850 6050 4900 6050
Wire Wire Line
	5850 5700 5850 5650
Wire Wire Line
	5850 5650 4900 5650
Wire Wire Line
	5850 5500 5850 5450
Wire Wire Line
	4900 5450 5850 5450
Wire Wire Line
	5850 5300 5850 5250
Wire Wire Line
	5850 5250 4900 5250
Wire Wire Line
	4900 5050 5850 5050
Wire Wire Line
	5850 5050 5850 5100
Wire Wire Line
	5850 4900 5850 4850
Wire Wire Line
	5850 4850 4900 4850
Wire Wire Line
	4900 4650 5850 4650
Wire Wire Line
	5850 4650 5850 4700
Wire Wire Line
	5850 4500 5850 4450
Wire Wire Line
	5850 4450 4900 4450
Wire Wire Line
	4900 4250 5850 4250
Wire Wire Line
	5850 4250 5850 4300
Wire Wire Line
	5850 4300 5950 4300
Wire Wire Line
	7050 4300 6950 4300
Wire Wire Line
	7050 4500 6950 4500
Wire Wire Line
	7050 4700 6950 4700
Wire Wire Line
	7050 4900 6950 4900
Wire Wire Line
	7050 5100 6950 5100
Wire Wire Line
	7050 5300 6950 5300
Wire Wire Line
	7050 5500 6950 5500
Wire Wire Line
	7050 5700 6950 5700
Wire Wire Line
	7050 5900 6950 5900
Wire Wire Line
	7050 6100 6950 6100
Wire Wire Line
	6950 5900 6950 5850
Wire Wire Line
	6950 6100 6950 6050
Wire Wire Line
	6950 5700 6950 5650
Wire Wire Line
	6950 5500 6950 5450
Wire Wire Line
	6950 5300 6950 5250
Wire Wire Line
	6950 5050 6950 5100
Wire Wire Line
	6950 4900 6950 4850
Wire Wire Line
	6950 4650 6950 4700
Wire Wire Line
	6950 4500 6950 4450
Wire Wire Line
	6950 4250 6950 4300
Wire Wire Line
	4900 4250 4900 4300
Connection ~ 4900 4300
Wire Wire Line
	4900 4300 4850 4300
Wire Wire Line
	4900 4450 4900 4500
Connection ~ 4900 4500
Wire Wire Line
	4900 4500 4850 4500
Wire Wire Line
	4900 4650 4900 4700
Connection ~ 4900 4700
Wire Wire Line
	4900 4700 4850 4700
Wire Wire Line
	4900 4850 4900 4900
Connection ~ 4900 4900
Wire Wire Line
	4900 4900 4850 4900
Wire Wire Line
	4900 5050 4900 5100
Connection ~ 4900 5100
Wire Wire Line
	4900 5100 4850 5100
Wire Wire Line
	4900 5250 4900 5300
Connection ~ 4900 5300
Wire Wire Line
	4900 5300 4850 5300
Wire Wire Line
	4900 5450 4900 5500
Connection ~ 4900 5500
Wire Wire Line
	4900 5500 4850 5500
Wire Wire Line
	4900 5650 4900 5700
Connection ~ 4900 5700
Wire Wire Line
	4900 5700 4850 5700
Wire Wire Line
	4900 5850 4900 5900
Connection ~ 4900 5900
Wire Wire Line
	4900 5900 4850 5900
Wire Wire Line
	4900 6050 4900 6100
Connection ~ 4900 6100
Wire Wire Line
	4900 6100 4850 6100
Wire Wire Line
	5950 6050 5950 6100
Wire Wire Line
	5950 6050 6950 6050
Connection ~ 5950 6100
Wire Wire Line
	5950 5900 5950 5850
Wire Wire Line
	5950 5850 6950 5850
Connection ~ 5950 5900
Wire Wire Line
	5950 5700 5950 5650
Wire Wire Line
	5950 5650 6950 5650
Connection ~ 5950 5700
Wire Wire Line
	5950 5500 5950 5450
Wire Wire Line
	5950 5450 6950 5450
Connection ~ 5950 5500
Wire Wire Line
	5950 5300 5950 5250
Wire Wire Line
	5950 5250 6950 5250
Connection ~ 5950 5300
Wire Wire Line
	5950 5100 5950 5050
Wire Wire Line
	5950 5050 6950 5050
Connection ~ 5950 5100
Wire Wire Line
	5950 4900 5950 4850
Wire Wire Line
	5950 4850 6950 4850
Connection ~ 5950 4900
Wire Wire Line
	5950 4700 5950 4650
Wire Wire Line
	5950 4650 6950 4650
Connection ~ 5950 4700
Wire Wire Line
	5950 4500 5950 4450
Wire Wire Line
	5950 4450 6950 4450
Connection ~ 5950 4500
Wire Wire Line
	5950 4300 5950 4250
Wire Wire Line
	5950 4250 6950 4250
Connection ~ 5950 4300
$Comp
L Device:LED D31
U 1 1 6201E660
P 7100 2650
F 0 "D31" V 7047 2730 50  0000 L CNN
F 1 "LED" V 7138 2730 50  0000 L CNN
F 2 "" H 7100 2650 50  0001 C CNN
F 3 "~" H 7100 2650 50  0001 C CNN
	1    7100 2650
	0    1    1    0   
$EndComp
$Comp
L Device:R_Small_US R1
U 1 1 620337BE
P 7100 2900
F 0 "R1" H 7168 2946 50  0000 L CNN
F 1 "R_Small_US" H 7168 2855 50  0000 L CNN
F 2 "" H 7100 2900 50  0001 C CNN
F 3 "~" H 7100 2900 50  0001 C CNN
	1    7100 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	7100 2500 7100 2400
Wire Wire Line
	7000 3000 7100 3000
Wire Wire Line
	8600 1800 8600 3400
Wire Wire Line
	7150 1900 7150 1300
Wire Wire Line
	6850 1300 6850 1700
$Comp
L Analog_ADC:MCP3426-xMS U1
U 1 1 620AAD54
P 5100 900
F 0 "U1" H 5100 1481 50  0000 C CNN
F 1 "MCP3426-xMS" H 5100 1390 50  0000 C CNN
F 2 "" H 5100 900 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/22226a.pdf" H 5100 900 50  0001 C CNN
	1    5100 900 
	1    0    0    -1  
$EndComp
Wire Wire Line
	3950 700  3950 1900
Wire Wire Line
	3950 700  4700 700 
Wire Wire Line
	4000 1800 4000 800 
Wire Wire Line
	4000 800  4700 800 
Wire Wire Line
	4050 1700 4050 900 
Wire Wire Line
	4050 900  4700 900 
Wire Wire Line
	4050 1700 5300 1700
Wire Wire Line
	4700 1000 4700 1250
Wire Wire Line
	8300 1800 8300 3600
Wire Wire Line
	3800 3100 5300 3100
Wire Wire Line
	5300 3000 3700 3000
Wire Wire Line
	3600 2800 5300 2800
Wire Wire Line
	5300 2600 3400 2600
Wire Wire Line
	5300 2500 3300 2500
Wire Wire Line
	3150 2300 5300 2300
Wire Wire Line
	3050 2200 5300 2200
Wire Wire Line
	2950 2100 5300 2100
Wire Wire Line
	2850 2000 5300 2000
Wire Wire Line
	3950 1900 5300 1900
Wire Wire Line
	5300 1800 4000 1800
$Comp
L MCU_RaspberryPi_and_Boards:Pico U2
U 1 1 62146EC9
P 6000 2650
F 0 "U2" H 6000 3865 50  0000 C CNN
F 1 "Pico" H 6000 3774 50  0000 C CNN
F 2 "RPi_Pico:RPi_Pico_SMD_TH" V 6000 2650 50  0001 C CNN
F 3 "" H 6000 2650 50  0001 C CNN
	1    6000 2650
	1    0    0    -1  
$EndComp
Wire Wire Line
	2850 2000 2850 6100
Wire Wire Line
	2950 2100 2950 5900
Wire Wire Line
	3050 2200 3050 5700
Wire Wire Line
	3150 2300 3150 5500
Wire Wire Line
	3300 2500 3300 5300
Wire Wire Line
	3400 2600 3400 5100
Wire Wire Line
	3500 2700 3500 4900
Wire Wire Line
	5300 2700 3500 2700
Wire Wire Line
	6100 3800 7900 3800
Wire Wire Line
	7100 2400 6700 2400
Wire Wire Line
	6700 2800 7000 2800
Wire Wire Line
	7000 2800 7000 3000
Wire Wire Line
	6850 1700 6750 1700
Wire Wire Line
	4700 1250 6750 1250
Connection ~ 6750 1700
Wire Wire Line
	6750 1700 6700 1700
Wire Wire Line
	7150 1900 6700 1900
Wire Wire Line
	8100 2100 6700 2100
Wire Wire Line
	6700 3500 8400 3500
Wire Wire Line
	8300 3600 6700 3600
Wire Wire Line
	6700 3400 8600 3400
$Comp
L Device:Battery_Cell BT1
U 1 1 6206E0F2
P 7050 1300
F 0 "BT1" V 6795 1350 50  0000 C CNN
F 1 "Battery_Cell 5v" V 6886 1350 50  0000 C CNN
F 2 "" V 7050 1360 50  0001 C CNN
F 3 "~" V 7050 1360 50  0001 C CNN
	1    7050 1300
	0    -1   1    0   
$EndComp
Wire Wire Line
	6750 1250 6750 1700
$EndSCHEMATC
