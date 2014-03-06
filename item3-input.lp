/* Objective function */
min: +Mon +Tue +Wed +Thu +Fri +Sat +Sun;

/* Constraints */
TotalMon: +Mon +Thu +Fri +Sat +Sun >= 11;
TotalTue: +Mon +Tue +Fri +Sat +Sun >= 7;
TotalWed: +Mon +Tue +Wed +Sat +Sun >= 6;
TotakThu: +Mon +Tue +Wed +Thu +Sun >= 9;
TotalFri: +Mon +Tue +Wed +Thu +Fri >= 12;
TotalSat: +Tue +Wed +Thu +Fri +Sat >= 5;
TotalSun: +Wed +Thu +Fri +Sat +Sun >= 8;

/* Integer definitions */
int Mon,Tue,Wed,Thu,Fri,Sat,Sun;
