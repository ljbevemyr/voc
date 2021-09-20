package org.python.stdlib.datetime;

import java.lang.Math;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class TimeDelta extends org.python.types.Object {

    @org.python.Attribute
    public org.python.Object days = __days__();

    @org.python.Attribute
    public org.python.Object seconds = __seconds__();

    @org.python.Attribute
    public org.python.Object microseconds = __microseconds__();

    @org.python.Attribute
    public org.python.Object min = __min__();
    @org.python.Attribute
    public org.python.Object max = __max__();
    @org.python.Attribute
    public org.python.Object resolution = __resolution__();

    @org.python.Method(__doc__ = "")
    public TimeDelta(org.python.Object[] args, java.util.Map<java.lang.String, org.python.Object> kwargs) {
	super();

	this.days = org.python.types.Int.getInt(0);
	this.seconds = org.python.types.Int.getInt(0);
	this.microseconds = org.python.types.Int.getInt(0);

	if (args.length > 7) {
	    throw new org.python.exceptions.TypeError("__new__() takes at most 7 arguments (" + args.length + " given)");
	}

	String[] allowed = { "days", "seconds", "microseconds", "milliseconds", "minutes", "hours", "weeks" };
	List<String> allowedList = Arrays.asList(allowed);
	if (!kwargs.isEmpty()) {
	    boolean correct = true;
	    for (java.lang.String key : kwargs.keySet()) {
		correct = allowedList.contains(key);
		if (!correct) {
		    throw new org.python.exceptions.TypeError(key + " is an invalid keuword argument for this function");

		}
	    }
	    if (args.length > 0) {
		if (kwargs.get("days") != null && args.length >= 1) {
		    throw new org.python.exceptions.TypeError("AAAAArgument given by name ('days') and position (1)");
		}

		if (kwargs.get("seconds") != null && args.length >= 2) {
		    throw new org.python.exceptions.TypeError("Argument given by name ('seconds') and position (2)");
		}

		if (kwargs.get("microseconds") != null && args.length >= 3) {
		    throw new org.python.exceptions.TypeError("Argument given by name ('microseconds') and position (3)");
		}
	    }
	}

	if (args.length == 7) {
        long days = ((org.python.types.Int) args[0]).value + ((org.python.types.Int) args[6]).value * 7;
	    this.days = org.python.types.Int.getInt(days);
        long seconds = ((org.python.types.Int) args[1]).value +
            ((org.python.types.Int) args[5]).value * 3600 + ((org.python.types.Int) args[4]).value * 60;
	    this.seconds = org.python.types.Int.getInt(seconds);
        long microseconds = ((org.python.types.Int) args[2]).value + ((org.python.types.Int) args[3]).value * 1000;
	    this.microseconds = org.python.types.Int.getInt(microseconds);
	}
    else if (args.length == 6) {
        this.days = args[0];
        long seconds = ((org.python.types.Int) args[1]).value +
            ((org.python.types.Int) args[5]).value * 3600 + ((org.python.types.Int) args[4]).value * 60;
        this.seconds = org.python.types.Int.getInt(seconds);
        long microseconds = ((org.python.types.Int) args[2]).value + ((org.python.types.Int) args[3]).value * 1000;
        this.microseconds = org.python.types.Int.getInt(microseconds);
	}
    else if (args.length == 5) {
        this.days = args[0];
        long seconds = ((org.python.types.Int) args[1]).value + ((org.python.types.Int) args[4]).value * 60;
        this.seconds = org.python.types.Int.getInt(seconds);
        long microseconds = ((org.python.types.Int) args[2]).value + ((org.python.types.Int) args[3]).value * 1000;
        this.microseconds = org.python.types.Int.getInt(microseconds);
	}
    else if (args.length == 4) {
        this.days = args[0];
        this.seconds = args[1];
        long microseconds = ((org.python.types.Int) args[2]).value + ((org.python.types.Int) args[3]).value * 1000;
        this.microseconds = org.python.types.Int.getInt(microseconds);
    }
    else if (args.length == 3) {
        this.days = args[0];
        this.seconds = args[1];
        this.microseconds = args[2];
    }
    else if (args.length == 2) {
        this.days = args[0];
        this.seconds = args[1];
        this.microseconds = org.python.types.Int.getInt(0);
    }
    else if (args.length == 1) {
        this.days = args[0];
        this.seconds = org.python.types.Int.getInt(0);
        this.microseconds = org.python.types.Int.getInt(0);
    }

	if (kwargs.get("weeks") != null) {
	    long weeks = ((org.python.types.Int) kwargs.get("weeks")).value;
	    long day = ((org.python.types.Int) this.days).value;
	    day = day + weeks * 7;
	    this.days = org.python.types.Int.getInt(day);
	}
    if (kwargs.get("days") != null) {
        long daysNew = ((org.python.types.Int) kwargs.get("days")).value;
        long daysOld = ((org.python.types.Int) this.days).value;
        daysNew = daysNew + daysOld;
        System.out.println(daysNew);
        this.days = org.python.types.Int.getInt(daysNew);
    }

	if (kwargs.get("hours") != null) {
	    long hours = ((org.python.types.Int) kwargs.get("hours")).value;
	    long second = ((org.python.types.Int) this.seconds).value;
	    second = second + hours * 3600;
	    this.seconds = org.python.types.Int.getInt(second);
	}

	if (kwargs.get("minutes") != null) {
	    long minutes = ((org.python.types.Int) kwargs.get("minutes")).value;
	    long minute = ((org.python.types.Int) this.seconds).value;
	    minute = minute + minutes * 60;
	    this.seconds = org.python.types.Int.getInt(minute);
	}

    if (kwargs.get("seconds") != null) {
        long secondsNew = ((org.python.types.Int) kwargs.get("seconds")).value;
        long secondsOld = ((org.python.types.Int) this.seconds).value;
        secondsNew = secondsNew + secondsOld;
        this.seconds = org.python.types.Int.getInt(secondsNew);
    }

	if (kwargs.get("milliseconds") != null) {
	    long millisecond = ((org.python.types.Int) kwargs.get("milliseconds")).value;
	    long mili = ((org.python.types.Int) this.microseconds).value;
	    mili = mili + millisecond * 1000;
	    this.microseconds = org.python.types.Int.getInt(mili);
	}
    if (kwargs.get("microseconds") != null) {
        long microsecondsNew = ((org.python.types.Int) kwargs.get("microseconds")).value;
        long microsecondsOld = ((org.python.types.Int) this.microseconds).value;
        microsecondsNew = microsecondsNew + microsecondsOld;
        this.microseconds = org.python.types.Int.getInt(microsecondsNew);
    }
    }

    @org.python.Method(__doc__ = "returns days")
    public org.python.types.Str __days__() {
	return new org.python.types.Str(this.days + "");
    }

    @org.python.Method(__doc__ = "returns month")
    public org.python.types.Str __seconds__() {
	return new org.python.types.Str(this.seconds + "");
    }

    @org.python.Method(__doc__ = "returns day")
    public org.python.types.Str __microseconds__() {
	return new org.python.types.Str(this.microseconds + "");
    }

    @org.python.Method()
    public org.python.Object __min__() {

	return new org.python.types.Str("-999999 days, 0:00:00");
    }

    @org.python.Method()
    public org.python.Object __max__() {
	return new org.python.types.Str("9999999 days, 23:59:59.999999");
    }

    @org.python.Method()
    public org.python.Object __resolution__() {
	return new org.python.types.Str("0:00:00.000001");
    }

    @org.python.Method()
    public org.python.types.Str total_seconds() {
	long days = (((org.python.types.Int) this.days).value) * 24 * 3600;
	long sum_seconds = days + (((org.python.types.Int) this.seconds).value);
	long microseconds = (((org.python.types.Int) this.microseconds).value);
	String micro = "";
	if (microseconds == 0) {
	    micro = "0";
	} else if (microseconds < 10) {
	    micro = "00000" + microseconds;
	} else if (microseconds < 100) {
	    micro = "0000" + microseconds;
	} else if (microseconds < 1000) {
	    micro = "000" + microseconds;
	} else if (microseconds < 10000) {
	    micro = "00" + microseconds;
	} else if (microseconds < 100000) {
	    micro = "0" + microseconds;
	} else {
	    micro = "" + microseconds;
	}
	String returnStr = ("" + sum_seconds + "." + micro);
	return new org.python.types.Str(returnStr);
    }

    @org.python.Method(__doc__ = "", args = { "other" })
    public org.python.Object __add__(org.python.Object other) {
	long thisDays = ((org.python.types.Int) this.days).value;
	TimeDelta otherObject = (org.python.stdlib.datetime.TimeDelta) other;
	long otherDays = ((org.python.types.Int) otherObject.days).value;
	long thisSeconds = ((org.python.types.Int) this.seconds).value;
	long otherSeconds = ((org.python.types.Int) otherObject.seconds).value;
	long thisMicroseconds = ((org.python.types.Int) this.microseconds).value;
	long otherMicroSeconds = ((org.python.types.Int) otherObject.microseconds).value;
	long sumDays = thisDays + otherDays;
	long sumSeconds = thisSeconds + otherSeconds;
	long sumMicroseconds = thisMicroseconds + otherMicroSeconds;
    if (sumMicroseconds > 999999) {
        long extraSeconds = sumMicroseconds / 1000000;
        sumMicroseconds = sumMicroseconds % 1000000;
        sumSeconds = sumSeconds + extraSeconds;
    }
    if (sumSeconds > 86399) {
        long extraDays = sumSeconds / 86400;
        sumSeconds = sumSeconds % 86400;
        sumDays = sumDays + extraDays;
    }
	org.python.Object[] args = { org.python.types.Int.getInt(sumDays), org.python.types.Int.getInt(sumSeconds), org.python.types.Int.getInt(sumMicroseconds) };
	TimeDelta TD = new TimeDelta(args, Collections.EMPTY_MAP);
	return TD;
    }

    @org.python.Method(__doc__ = "", args = { "other" })
    public org.python.Object __difference__(org.python.Object other) {
        long thisDays = ((org.python.types.Int) this.days).value;
        TimeDelta otherObject = (org.python.stdlib.datetime.TimeDelta) other;
        long otherDays = ((org.python.types.Int) otherObject.days).value;
        long thisSeconds = ((org.python.types.Int) this.seconds).value;
        long otherSeconds = ((org.python.types.Int) otherObject.seconds).value;
        long thisMicroseconds = ((org.python.types.Int) this.microseconds).value;
        long otherMicroSeconds = ((org.python.types.Int) otherObject.microseconds).value;
        long sumDays = thisDays - otherDays;
        long sumSeconds = thisSeconds - otherSeconds;
        long sumMicroseconds = thisMicroseconds - otherMicroSeconds;
        if (sumMicroseconds < 0) {
            sumSeconds = sumSeconds -1;
            sumMicroseconds = 1000000 + sumMicroseconds;
        }
        if (sumSeconds < 0) {
            sumDays = sumDays -1;
            sumSeconds = 86400 + sumSeconds;
        }
        org.python.Object[] args = { org.python.types.Int.getInt(sumDays), org.python.types.Int.getInt(sumSeconds), org.python.types.Int.getInt(sumMicroseconds) };
        TimeDelta TD = new TimeDelta(args, Collections.EMPTY_MAP);
        return TD;
    }

    @org.python.Method(__doc__ = "", args = { "constant" })
    public org.python.Object __multiplication__(long constant) {
        long thisDays = ((org.python.types.Int) this.days).value;
        long thisSeconds = ((org.python.types.Int) this.seconds).value;
        long thisMicroseconds = ((org.python.types.Int) this.microseconds).value;
        long sumMicroseconds = thisMicroseconds * constant;
        long sumSeconds = thisSeconds * constant;
        long sumDays = thisDays * constant;

        if (sumMicroseconds < 0) {
            long extraSeconds = (long) Math.ceil(-((double) sumMicroseconds / 1000000));
            sumMicroseconds = (-1 * sumMicroseconds) % 1000000;
            if (sumMicroseconds != 0 ) {
                sumMicroseconds = 1000000 - (sumMicroseconds);
            }
            sumSeconds = sumSeconds - extraSeconds;
        } else if (sumMicroseconds > 999999) {
            long extraSeconds = sumMicroseconds / 1000000;
            sumMicroseconds = sumMicroseconds % 1000000;
            sumSeconds = sumSeconds + extraSeconds;
        }

        if (sumSeconds < 0) {
            long extraDays = (long) Math.ceil(-((double) sumSeconds / 86400));
            sumSeconds = (-1 * sumSeconds) % 86400;
            if (sumSeconds != 0) {
                sumSeconds = 86400 - sumSeconds;
            }
            sumDays = sumDays - extraDays;
        } else if (sumSeconds > 86399) {
            long extraDays = sumSeconds / 86400;
            sumSeconds = sumSeconds % 86400;
            sumDays = sumDays + extraDays;
        }
        org.python.Object[] args = { org.python.types.Int.getInt(sumDays), org.python.types.Int.getInt(sumSeconds), org.python.types.Int.getInt(sumMicroseconds) };
        TimeDelta TD = new TimeDelta(args, Collections.EMPTY_MAP);
        return TD;
    }

    @org.python.Method(__doc__ = "", args = { "other" })
    public Boolean __equal__(org.python.Object other) {
        //FIXME: May be more robust to convert everyting to microseconds
        TimeDelta otherObject = (org.python.stdlib.datetime.TimeDelta) other;
        long thisDays = ((org.python.types.Int) this.days).value;
        long otherDays = ((org.python.types.Int) otherObject.days).value;
        long thisSeconds = ((org.python.types.Int) this.seconds).value;
        long otherSeconds = ((org.python.types.Int) otherObject.seconds).value;
        long thisMicroseconds = ((org.python.types.Int) this.microseconds).value;
        long otherMicroseconds = ((org.python.types.Int) otherObject.microseconds).value;
        Boolean days = thisDays == otherDays;
        Boolean seconds = thisSeconds == otherSeconds;
        Boolean microseconds = thisMicroseconds == otherMicroseconds;
        return (days && seconds && microseconds);
    }

    @org.python.Method(__doc__ = "", args = { "other" })
    public Boolean __notEqual__(org.python.Object other) {
        TimeDelta otherObject = (org.python.stdlib.datetime.TimeDelta) other;
        long thisDays = ((org.python.types.Int) this.days).value;
        long otherDays = ((org.python.types.Int) otherObject.days).value;
        long thisSeconds = ((org.python.types.Int) this.seconds).value;
        long otherSeconds = ((org.python.types.Int) otherObject.seconds).value;
        long thisMicroseconds = ((org.python.types.Int) this.microseconds).value;
        long otherMicroseconds = ((org.python.types.Int) otherObject.microseconds).value;
        Boolean days = thisDays != otherDays;
        Boolean seconds = thisSeconds != otherSeconds;
        Boolean microseconds = thisMicroseconds != otherMicroseconds;
        return (days || seconds || microseconds);
    }

    @org.python.Method(__doc__ = "", args = { "other" })
    public Boolean __lessThan__(org.python.Object other) {
        TimeDelta otherObject = (org.python.stdlib.datetime.TimeDelta) other;
        long thisDays = ((org.python.types.Int) this.days).value;
        long otherDays = ((org.python.types.Int) otherObject.days).value;
        long thisSeconds = ((org.python.types.Int) this.seconds).value;
        long otherSeconds = ((org.python.types.Int) otherObject.seconds).value;
        long thisMicroseconds = ((org.python.types.Int) this.microseconds).value;
        long otherMicroseconds = ((org.python.types.Int) otherObject.microseconds).value;
        if (thisDays < otherDays) {
            return true;
        }
        if (thisSeconds < otherSeconds) {
            return true;
        }
        if (thisMicroseconds < otherMicroseconds) {
            return true;
        }
        return false;
    }

    @org.python.Method(__doc__ = "", args = { "other" })
    public Boolean __lessOrEqualThan__(org.python.Object other) {
        TimeDelta otherObject = (org.python.stdlib.datetime.TimeDelta) other;
        long thisDays = ((org.python.types.Int) this.days).value;
        long otherDays = ((org.python.types.Int) otherObject.days).value;
        long thisSeconds = ((org.python.types.Int) this.seconds).value;
        long otherSeconds = ((org.python.types.Int) otherObject.seconds).value;
        long thisMicroseconds = ((org.python.types.Int) this.microseconds).value;
        long otherMicroseconds = ((org.python.types.Int) otherObject.microseconds).value;
        if (thisDays < otherDays) {
            return true;
        }
        if (thisSeconds < otherSeconds) {
            return true;
        }
        if (thisMicroseconds < otherMicroseconds) {
            return true;
        }
        Boolean days = thisDays == otherDays;
        Boolean seconds = thisSeconds == otherSeconds;
        Boolean microseconds = thisMicroseconds == otherMicroseconds;
        return (days && seconds && microseconds);
    }

    @org.python.Method(__doc__ = "", args = { "other" })
    public Boolean __greaterThan__(org.python.Object other) {
        TimeDelta otherObject = (org.python.stdlib.datetime.TimeDelta) other;
        long thisDays = ((org.python.types.Int) this.days).value;
        long otherDays = ((org.python.types.Int) otherObject.days).value;
        long thisSeconds = ((org.python.types.Int) this.seconds).value;
        long otherSeconds = ((org.python.types.Int) otherObject.seconds).value;
        long thisMicroseconds = ((org.python.types.Int) this.microseconds).value;
        long otherMicroseconds = ((org.python.types.Int) otherObject.microseconds).value;
        if (thisDays > otherDays) {
            return true;
        }
        if (thisSeconds > otherSeconds) {
            return true;
        }
        if (thisMicroseconds > otherMicroseconds) {
            return true;
        }
        return false;
    }

    @org.python.Method(__doc__ = "", args = { "other" })
    public Boolean __greaterOrEqualThan__(org.python.Object other) {
        TimeDelta otherObject = (org.python.stdlib.datetime.TimeDelta) other;
        long thisDays = ((org.python.types.Int) this.days).value;
        long otherDays = ((org.python.types.Int) otherObject.days).value;
        long thisSeconds = ((org.python.types.Int) this.seconds).value;
        long otherSeconds = ((org.python.types.Int) otherObject.seconds).value;
        long thisMicroseconds = ((org.python.types.Int) this.microseconds).value;
        long otherMicroseconds = ((org.python.types.Int) otherObject.microseconds).value;
        if (thisDays > otherDays) {
            return true;
        }
        if (thisSeconds > otherSeconds) {
            return true;
        }
        if (thisMicroseconds > otherMicroseconds) {
            return true;
        }
        Boolean days = thisDays == otherDays;
        Boolean seconds = thisSeconds == otherSeconds;
        Boolean microseconds = thisMicroseconds == otherMicroseconds;
        return (days && seconds && microseconds);
    }

    public org.python.Object __pos__() {
	long otherSeconds = ((org.python.types.Int) this.seconds).value;
	long otherMicroSeconds = ((org.python.types.Int) this.microseconds).value;
	long otherDays = ((org.python.types.Int) this.days).value;
	org.python.Object[] args = { org.python.types.Int.getInt(otherDays), org.python.types.Int.getInt(otherSeconds), org.python.types.Int.getInt(otherMicroSeconds) };
	TimeDelta TD = new TimeDelta(args, Collections.EMPTY_MAP);
	return TD;
    }

    public org.python.types.Str __str__() {
	long dayslong = ((org.python.types.Int) this.days).value;
	String days = Long.toString(dayslong);
	long seconds = ((org.python.types.Int) this.seconds).value;
	long microseconds = ((org.python.types.Int) this.microseconds).value;
	String returnStr = days + " days, " + "seconds: " + seconds + ", microseconds: " + microseconds;
	return new org.python.types.Str(returnStr);
    }

    @org.python.Method(__doc__ = "")
    public static org.python.Object constant_4() {
	return org.python.types.Int.getInt(4);
    }
}
