import org.junit.Test;
import org.python.Object;
import org.python.stdlib.datetime.TimeDelta;
import org.python.types.Int;

import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.assertEquals;

public class TimeDeltaTests {
    public static TimeDelta initDelta(double days,double seconds,double microseconds,double  milliseconds,
            double minutes,double hours,double  weeks) {
        Map<String, Object> kwargs = new HashMap<>();
        kwargs.put("days", Int.getInt(10));
        //kwargs.put("seconds", new Int.getInt(seconds));
        //kwargs.put("microseconds", new Int.getInt(microseconds));
        //kwargs.put("milliseconds", new Int.getInt(milliseconds));
        //kwargs.put("minutes", new Int.getInt(minutes));
        //kwargs.put("hours", new Int.getInt(hours));
        //kwargs.put("weeks", new Int.getInt(weeks));
        org.python.Object[] allowed = new Object[1];
        return new TimeDelta(allowed, kwargs);
    }

    @Test
    public void superSimple(){
        TimeDelta time = initDelta(1,1,1,1,1,1,1);
        assertEquals(1,time.days);
    }

}
