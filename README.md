# contiki_app

### Author: Abid Khaled
This work is done during my End of Studies internship (research internship) in collaboration with UMR Heudiasyc Laboratory in Université de Technologie de Compiègne "UTC".

Contiki_app is a repository which contains two parts:
## 1- Data Formatting:
This file is responsible for:
- Network log data formatting: from the log file extracted from Cooja simulator it inspects its lines and build a dataframe which contains essential information to caracterise the network energy state over time.
Also it applies Energy Harvesting for given nodes in the network depending on irradiation values in a csv file (columbia_irr_only_no_gaps.csv).

## 2- Data Visualization:
- Network energy state visualization: Multiple plots which describe the energetic state of the network and nodes.
