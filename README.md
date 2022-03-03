# Trex miner shares calculator
## Description
 a simple Python program that reads the log files of T-rex miner and displays the number of shares. works as a contribution measure when mining with multiple rigs that are associated with one Wallet.
 
### Features:
 
	- a simple GUI	
	- Path and data are saved for the next the program is run
	
## How to use

 1- add the log option inside the T-rex mining batch file: --log-path :a_folder_where_logs_will_saved\RigName.log
 
 2- run TrexSharesCalculator.py (Requires Python installed on current computer)
 
 3- click on add new rig and write the rig name which should be the same as the one specified in the batch file (RigName)
 
 4- write the path of the folder that has the log files (:a_folder_where_logs_will_saved) and click update Path
 
 5- click on Calculate Shares
 
 Notes: the program will create two .pkl files which will store the last path configuration and the stored data from last calculation

## How it works:

 By analyzing text, the program extracts confirmed shares and store them as shares datatype. the shares are written/read externally using pickle module.

## Acknowledgments

 Check out T-Rex miner offical github page: https://github.com/trexminer/T-Rex
