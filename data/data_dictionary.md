# LTFS Vehicle Loan Default Prediction - Data Dictionary

| Variable Name | Definition | Type |
|---|---|---|
| `UniqueID` | Identifier for loan/applicant | Identifier |
| `disbursed_amount` | Amount disbursed for the loan (INR) | Continuous (Numerical) |
| `asset_cost` | Total cost of the vehicle / asset (INR) | Continuous (Numerical) |
| `ltv` | Loan to Value ratio (%) | Continuous (Numerical) |
| `branch_id` | Branch where loan was disbursed | Categorical (Identifier) |
| `supplier_id` | Vehicle dealer / dealership ID | Categorical (Identifier) |
| `manufacturer_id` | Vehicle manufacturer ID | Categorical (Identifier) |
| `Current_pincode_ID` | Postal code of the customer's current address | Categorical (Identifier) |
| `Date.of.Birth` | Date of birth of the borrower (DD-MM-YY) | Date / String |
| `Employment.Type` | Employment status (`Salaried`, `Self employed`, `NaN`) | Categorical |
| `DisbursalDate` | Date on which the loan was disbursed (DD-MM-YY) | Date / String |
| `State_ID` | State where loan was disbursed | Categorical |
| `Employee_code_ID` | Employee ID who disbursed the loan | Categorical (Identifier) |
| `MobileNo_Avl_Flag` | Mobile number provided flag (1: Yes, 0: No) | Binary Flag |
| `Aadhar_flag` | Aadhaar card submitted flag (1: Yes, 0: No) | Binary Flag |
| `PAN_flag` | PAN card submitted flag (1: Yes, 0: No) | Binary Flag |
| `VoterID_flag` | Voter ID submitted flag (1: Yes, 0: No) | Binary Flag |
| `Driving_flag` | Driving license submitted flag (1: Yes, 0: No) | Binary Flag |
| `Passport_flag` | Passport submitted flag (1: Yes, 0: No) | Binary Flag |
| `PERFORM_CNS.SCORE` | CRISIL/HighMark Bureau credit score (0 to 890; 0 = No history) | Discrete (Numerical) |
| `PERFORM_CNS.SCORE.DESCRIPTION` | Credit bureau risk rating/classification | Categorical |
| `PRI.NO.OF.ACCTS` | Primary total number of credit accounts | Discrete (Numerical) |
| `PRI.ACTIVE.ACCTS` | Primary number of active credit accounts | Discrete (Numerical) |
| `PRI.OVERDUE.ACCTS` | Primary number of overdue/default accounts | Discrete (Numerical) |
| `PRI.CURRENT.BALANCE` | Primary total outstanding balance across accounts | Continuous (Numerical) |
| `PRI.SANCTIONED.AMOUNT` | Primary total sanctioned loan amount | Continuous (Numerical) |
| `PRI.DISBURSED.AMOUNT` | Primary total disbursed loan amount | Continuous (Numerical) |
| `SEC.NO.OF.ACCTS` | Secondary (co-applicant/guarantor) total credit accounts | Discrete (Numerical) |
| `SEC.ACTIVE.ACCTS` | Secondary number of active credit accounts | Discrete (Numerical) |
| `SEC.OVERDUE.ACCTS` | Secondary number of overdue accounts | Discrete (Numerical) |
| `SEC.CURRENT.BALANCE` | Secondary total current balance | Continuous (Numerical) |
| `SEC.SANCTIONED.AMOUNT` | Secondary total sanctioned amount | Continuous (Numerical) |
| `SEC.DISBURSED.AMOUNT` | Secondary total disbursed amount | Continuous (Numerical) |
| `PRIMARY.INSTAL.AMT` | Monthly installment (EMI) amount for primary accounts | Continuous (Numerical) |
| `SEC.INSTAL.AMT` | Monthly installment (EMI) amount for secondary accounts | Continuous (Numerical) |
| `NEW.ACCTS.IN.LAST.SIX.MONTHS` | Accounts opened within the last 6 months | Discrete (Numerical) |
| `DELINQUENT.ACCTS.IN.LAST.SIX.MONTHS`| Delinquent accounts in the last 6 months | Discrete (Numerical) |
| `AVERAGE.ACCT.AGE` | Average tenure of credit accounts (e.g. `'1yrs 11mon'`) | String / Duration |
| `CREDIT.HISTORY.LENGTH` | Time elapsed since first credit account opening | String / Duration |
| `NO.OF_INQUIRIES` | Number of inquiries made by customer for loans | Discrete (Numerical) |
| `loan_default` | **Target:** 1 if applicant defaulted on 1st EMI, 0 otherwise | Binary Target |

