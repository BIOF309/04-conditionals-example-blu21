#Billy Lu, Conditionals Example

#This program takes in acronyms of NIH institutes, centers, and offices and outputs their full names.

#allows user to input the acronym of an NIH institute, center, or office
nih_input = input ("Enter the acronym of an NIH institute, center, or office (upper or lower case): ")

#capitalizes the letters of the acronyms
nih = nih_input.upper()

if nih == "OD":
    print (nih, "= NIH office of the Director")
elif nih == "NCI":
    print (nih, "= National Cancer Institute")
elif nih == "NEI":
    print (nih, "= National Eye Institute")
elif nih == "NHLBI":
    print (nih, "= National Heart, Lung, and Blood Institute")
elif nih == "NHGRI":
    print (nih, "= National Hume Genome Research Institute")
elif nih == "NIA":
    print (nih, "= National Institute on Aging")
elif nih == "NIAAA":
    print (nih, "= National Institute on ALcohol Abuse and Alcoholism")
elif nih == "NIAID":
    print (nih, "= National Institute of Allergy and Infectious Diseases")
elif nih == "NIAMS":
    print (nih, "= National Institute of Arthritis and Musculoskeletal and Skin Diseases")
elif nih == "NIBIB":
    print (nih, "= National Institute of Biomedical Imaging and Bioengineering")
elif nih == "NICHD":
    print (nih, "= National Institute of Child Health and Human Development")
elif nih == "NIDCD":
    print (nih, "= National Institute on Deafness and Other Communication Disorders")
elif nih == "NIDCR":
    print (nih, "= National Institute of Dental and Craniofacial Research")
elif nih == "NIDDK":
    print (nih, "= National Institute of Diabetes and Digestive and Kidney Diseases")
elif nih == "NIDA":
    print (nih, "= National Institute on Drug Abuse")
elif nih == "NIEHS":
    print (nih, "= National Institute of Environmental Health Science")
elif nih == "NIGMS":
    print (nih, "= National Institute of General Medical Sciences")
elif nih == "NIMH":
    print (nih, "= National Institute of Mental Health")
elif nih == "NIMHD":
    print (nih, "= National Institute on Minority Health and Health Disparaties")
elif nih == "NINDS":
    print (nih, "= National Institute of Neurological Disorders and Stroke")
elif nih == "NINR":
    print (nih, "= National Institute of Nursing Research")
elif nih == "NLM":
    print (nih, "= National Library of Medicine")
elif nih == "CC":
    print (nih, "= NIH Clinical Center")
elif nih == "CIT":
    print (nih, "= Center for Information Technology")
elif nih == "CSR":
    print (nih, "= Center for Scientific Review")
elif nih == "FIC":
    print (nih, "= Fogarty International Center")
elif nih == "NCATS":
    print (nih, "= National Center for Advancing Translational Sciences")
elif nih == "NCCIH":
    print (nih, "= National Center for Complementary and Integrative Health")
else:
    print ("You did not enter a valid NIH institute, center, or office")
