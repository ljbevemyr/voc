import org.junit.Test;
import org.python.Object;
import org.python.exceptions.TypeError;
import org.python.stdlib.datetime.TimeDelta;
import org.python.types.Int;
import org.python.types.Str;

import java.util.*;

import static org.junit.Assert.*;

public class TimeDeltaTests {
    public static TimeDelta initDelta(List<Integer> argsOld, Map<String, Object> kwargs) {
        org.python.Object[] argsNew = new Object[argsOld.size()];
        for (int i = 0; i < argsOld.size(); i++) {
            argsNew[i] = org.python.types.Int.getInt(argsOld.get(i));
        }
        return new TimeDelta(argsNew, kwargs);
    }

    @Test
    public void superSimpleKwarg(){
        Map<String, Object> kwargs = new HashMap<>();
        kwargs.put("days", Int.getInt(1));
        kwargs.put("seconds", Int.getInt(1));
        kwargs.put("microseconds", Int.getInt(1));
        kwargs.put("milliseconds", Int.getInt(1));
        kwargs.put("minutes", Int.getInt(1));
        kwargs.put("hours", Int.getInt(1));
        kwargs.put("weeks", Int.getInt(1));

        List args = new ArrayList();
        TimeDelta time = initDelta(args, kwargs);
        assertEquals(org.python.types.Int.getInt(8),time.days);
        assertEquals(org.python.types.Int.getInt(3661),time.seconds);
        assertEquals(org.python.types.Int.getInt(1001),time.microseconds);
    }

    @Test
    public void superSimpleArg() {
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        TimeDelta time = initDelta(args, kwargs);
        assertEquals(org.python.types.Int.getInt(8), time.days);
        assertEquals(org.python.types.Int.getInt(3661), time.seconds);
        assertEquals(org.python.types.Int.getInt(1001), time.microseconds);
    }

    @Test
    public void NegativeValuesArg(){
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args = Arrays.asList(1, -20000, -200000, 0, 0, 0, 0);
        TimeDelta time = initDelta(args, kwargs);
        assertEquals(org.python.types.Int.getInt(0),time.days);
        assertEquals(org.python.types.Int.getInt(66399),time.seconds);
        assertEquals(org.python.types.Int.getInt(800000),time.microseconds);
    }

    @Test
    public void BigValuesArg(){
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args = Arrays.asList(1, 20000, 1000000, 0, 0, 0, 0);
        TimeDelta time = initDelta(args, kwargs);
        assertEquals(org.python.types.Int.getInt(1),time.days);
        assertEquals(org.python.types.Int.getInt(20001),time.seconds);
        assertEquals(org.python.types.Int.getInt(0),time.microseconds);
    }

    @Test
    public void WrongValuesArg(){
        Map<String, Object> kwargs = new HashMap<>();
        kwargs.put("days", Int.getInt(1));
        kwargs.put("seconds", Int.getInt(1));
        kwargs.put("microseconds", Int.getInt(1));
        kwargs.put("milliseconds", Int.getInt(1));
        kwargs.put("minutes", Int.getInt(1));
        kwargs.put("hours", Int.getInt(1));
        kwargs.put("weeks", Int.getInt(1));

        Map<String, Object> kwargsWrongKey = new HashMap<>();
        kwargsWrongKey.put("weeksss", Int.getInt(1));

        List<Integer> args = Arrays.asList(1, 20000, 1000000, 0, 0, 0, 0);
        List<Integer> args0 = Arrays.asList();
        TypeError error = assertThrows(TypeError.class, () -> initDelta(args, kwargs));
        assertEquals("Argument given by name ('days') and position (1)", error.getMessage());
        TypeError error0 = assertThrows(TypeError.class, () -> initDelta(args0, kwargsWrongKey));
        assertEquals("weeksss is an invalid keyword argument for this function", error0.getMessage());
    }

    @Test
    public void AddArg() {
        //TODO: Test negative values
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args0 = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        List<Integer> args1 = Arrays.asList(0, 86399, 999999, 0, 0, 0, 0);
        TimeDelta time1 = initDelta(args0, kwargs);
        TimeDelta time2 = initDelta(args0, kwargs);
        TimeDelta time3 = initDelta(args1, kwargs);
        TimeDelta time4 = initDelta(args1, kwargs);
        TimeDelta timeAdded0 = (TimeDelta) time1.__add__(time2);
        TimeDelta timeAdded1 = (TimeDelta) time3.__add__(time4);
        assertEquals(org.python.types.Int.getInt(16), timeAdded0.days);
        assertEquals(org.python.types.Int.getInt(7322), timeAdded0.seconds);
        assertEquals(org.python.types.Int.getInt(2002), timeAdded0.microseconds);
        assertEquals(org.python.types.Int.getInt(1), timeAdded1.days);
        assertEquals(org.python.types.Int.getInt(86399), timeAdded1.seconds);
        assertEquals(org.python.types.Int.getInt(999998), timeAdded1.microseconds);
    }

    @Test
    public void DifferenceArg() {
        //TODO: Test negative values
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args0 = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        List<Integer> args1 = Arrays.asList(0, 0, 0, 0, 0, 0, 0);
        List<Integer> args2 = Arrays.asList(0, 86399, 999999, 0, 0, 0, 0);
        TimeDelta time1 = initDelta(args0, kwargs);
        TimeDelta time2 = initDelta(args0, kwargs);
        TimeDelta time3 = initDelta(args1, kwargs);
        TimeDelta time4 = initDelta(args2, kwargs);
        TimeDelta timeDiff0 = (TimeDelta) time1.__difference__(time2);
        TimeDelta timeDiff1 = (TimeDelta) time3.__difference__(time4);
        assertEquals(org.python.types.Int.getInt(0), timeDiff0.days);
        assertEquals(org.python.types.Int.getInt(0), timeDiff0.seconds);
        assertEquals(org.python.types.Int.getInt(0), timeDiff0.microseconds);
        assertEquals(org.python.types.Int.getInt(-1), timeDiff1.days);
        assertEquals(org.python.types.Int.getInt(0), timeDiff1.seconds);
        assertEquals(org.python.types.Int.getInt(1), timeDiff1.microseconds);
    }

    @Test
    public void MultiplicationArg() {
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args00 = Arrays.asList(1, 1, 0, 0, 0, 0, 0);
        List<Integer> args0 = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        List<Integer> args1 = Arrays.asList(0, 0, 0, 0, 0, 0, 0);
        List<Integer> args2 = Arrays.asList(0, 86399, 999999, 0, 0, 0, 0);
        TimeDelta time00 = initDelta(args00, kwargs);
        TimeDelta time0 = initDelta(args0, kwargs);
        TimeDelta time1 = initDelta(args1, kwargs);
        TimeDelta time2 = initDelta(args2, kwargs);

        TimeDelta timeMult00 = (TimeDelta) time00.__multiplication__(999998);
        assertEquals(org.python.types.Int.getInt(0), timeMult00.microseconds);
        assertEquals(org.python.types.Int.getInt(49598), timeMult00.seconds);
        assertEquals(org.python.types.Int.getInt(1000009), timeMult00.days);

        TimeDelta timeMult0 = (TimeDelta) time0.__multiplication__(999998);
        assertEquals(org.python.types.Int.getInt(997998), timeMult0.microseconds);
        assertEquals(org.python.types.Int.getInt(52878), timeMult0.seconds);
        assertEquals(org.python.types.Int.getInt(8042356), timeMult0.days);

        TimeDelta timeMult1 = (TimeDelta) time1.__multiplication__(123456);
        assertEquals(org.python.types.Int.getInt(0), timeMult1.days);
        assertEquals(org.python.types.Int.getInt(0), timeMult1.seconds);
        assertEquals(org.python.types.Int.getInt(0), timeMult1.microseconds);

        TimeDelta timeMult2 = (TimeDelta) time2.__multiplication__(0);
        assertEquals(org.python.types.Int.getInt(0), timeMult2.days);
        assertEquals(org.python.types.Int.getInt(0), timeMult2.seconds);
        assertEquals(org.python.types.Int.getInt(0), timeMult2.microseconds);

        TimeDelta timeMult3 = (TimeDelta) time2.__multiplication__(999998);
        assertEquals(org.python.types.Int.getInt(999997), timeMult3.days);
        assertEquals(org.python.types.Int.getInt(86399), timeMult3.seconds);
        assertEquals(org.python.types.Int.getInt(2), timeMult3.microseconds);

        TimeDelta timeMult4 = (TimeDelta) time2.__multiplication__(-2);
        assertEquals(org.python.types.Int.getInt(2), timeMult4.microseconds);
        assertEquals(org.python.types.Int.getInt(0), timeMult4.seconds);
        assertEquals(org.python.types.Int.getInt(-2), timeMult4.days);

        TimeDelta timeMult5 = (TimeDelta) time2.__multiplication__(-999998);
        assertEquals(org.python.types.Int.getInt(999998), timeMult5.microseconds);
        assertEquals(org.python.types.Int.getInt(0), timeMult5.seconds);
        assertEquals(org.python.types.Int.getInt(-999998), timeMult5.days);


    }

    @Test
    public void EqualArg() {
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args0 = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        List<Integer> args1 = Arrays.asList(0, 1, 1, 1, 1, 1, 1);
        TimeDelta time1 = initDelta(args0, kwargs);
        TimeDelta time2 = initDelta(args0, kwargs);
        TimeDelta time3 = initDelta(args1, kwargs);
        Boolean timeComp = (Boolean) time1.__equal__(time2);
        Boolean timeCompFalse = (Boolean) time1.__equal__(time3);
        assertTrue(timeComp);
        assertFalse(timeCompFalse);
    }

    @Test
    public void NotEqualArg() {
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args0 = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        List<Integer> args1 = Arrays.asList(0, 1, 1, 1, 1, 1, 1);
        TimeDelta time1 = initDelta(args0, kwargs);
        TimeDelta time2 = initDelta(args0, kwargs);
        TimeDelta time3 = initDelta(args1, kwargs);
        Boolean timeComp = (Boolean) time1.__notEqual__(time3);
        Boolean timeCompFalse = (Boolean) time1.__notEqual__(time2);
        assertTrue(timeComp);
        assertFalse(timeCompFalse);
    }

    @Test
    public void lessThanArg() {
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args0 = Arrays.asList(1, 1, 1, 0, 1, 1, 1);
        List<Integer> args1 = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        TimeDelta time1 = initDelta(args0, kwargs);
        TimeDelta time2 = initDelta(args0, kwargs);
        TimeDelta time3 = initDelta(args1, kwargs);
        Boolean timeComp = (Boolean) time1.__lessThan__(time3);
        Boolean timeCompSameFalse = (Boolean) time1.__lessThan__(time2);
        Boolean timeCompFalse = (Boolean) time3.__lessThan__(time1);
        assertTrue(timeComp);
        assertFalse(timeCompSameFalse);
        assertFalse(timeCompFalse);
    }

    @Test
    public void lessOrEqualThanArg() {
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args0 = Arrays.asList(1, 1, 1, 0, 1, 1, 1);
        List<Integer> args1 = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        TimeDelta time1 = initDelta(args0, kwargs);
        TimeDelta time2 = initDelta(args0, kwargs);
        TimeDelta time3 = initDelta(args1, kwargs);
        Boolean timeComp = (Boolean) time1.__lessOrEqualThan__(time3);
        Boolean timeCompSame = (Boolean) time1.__lessOrEqualThan__(time2);
        Boolean timeCompFalse = (Boolean) time3.__lessOrEqualThan__(time1);
        assertTrue(timeComp);
        assertTrue(timeCompSame);
        assertFalse(timeCompFalse);
    }

    @Test
    public void greaterThanArg() {
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args0 = Arrays.asList(1, 1, 1, 0, 1, 1, 1);
        List<Integer> args1 = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        TimeDelta time1 = initDelta(args0, kwargs);
        TimeDelta time2 = initDelta(args0, kwargs);
        TimeDelta time3 = initDelta(args1, kwargs);
        Boolean timeComp = (Boolean) time3.__greaterThan__(time1);
        Boolean timeCompSameFalse = (Boolean) time1.__greaterThan__(time2);
        Boolean timeCompFalse = (Boolean) time1.__greaterThan__(time3);
        assertTrue(timeComp);
        assertFalse(timeCompSameFalse);
        assertFalse(timeCompFalse);
    }

    @Test
    public void greaterOrEqualThanArg() {
        Map<String, Object> kwargs = new HashMap<>();
        List<Integer> args0 = Arrays.asList(1, 1, 1, 0, 1, 1, 1);
        List<Integer> args1 = Arrays.asList(1, 1, 1, 1, 1, 1, 1);
        TimeDelta time1 = initDelta(args0, kwargs);
        TimeDelta time2 = initDelta(args0, kwargs);
        TimeDelta time3 = initDelta(args1, kwargs);
        Boolean timeComp = (Boolean) time3.__greaterOrEqualThan__(time1);
        Boolean timeCompSame = (Boolean) time1.__greaterOrEqualThan__(time2);
        Boolean timeCompFalse = (Boolean) time1.__greaterOrEqualThan__(time3);
        assertTrue(timeComp);
        assertTrue(timeCompSame);
        assertFalse(timeCompFalse);
    }
}
