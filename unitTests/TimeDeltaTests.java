import org.junit.Test;
import org.python.Object;
import org.python.stdlib.datetime.TimeDelta;
import org.python.types.Float;

import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.assertEquals;

public class TimeDeltaTests {
    public static TimeDelta initDelta(double weeks, double days, double hours, double minutes, double seconds,
                                      double milliseconds, double microseconds) {
        Map<String, Object> kwargs = new HashMap<>();
        kwargs.put("days", new Float(days));
        kwargs.put("seconds", new Float(seconds));
        kwargs.put("microseconds", new Float(microseconds));
        kwargs.put("milliseconds", new Float(milliseconds));
        kwargs.put("minutes", new Float(minutes));
        kwargs.put("hours", new Float(hours));
        kwargs.put("weeks", new Float(weeks));
        org.python.Object[] allowed = new Object[0];
        return new TimeDelta(allowed, kwargs);
    }

    @Test
    public void superSimple(){
        assertEquals(1, 1);
    }

}
