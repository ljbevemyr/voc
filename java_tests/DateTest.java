import org.junit.jupiter.api.Test;
import org.python.stdlib.datetime.Date;
import java.util.Collections;
import static org.junit.jupiter.api.Assertions.*;

class DateTest {

    @Test
    public void testInitialize1() {
        //testing Initialize with 3 args
        org.python.Object[] args = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(30)};
        java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<>();
        Date date = new Date(args, kwargs);
        assertEquals(new org.python.types.Str("30"), date.__day__());
        assertEquals(new org.python.types.Str("9"), date.__month__());
        assertEquals(new org.python.types.Str("2021"), date.__year__());
    }

    @Test
    public void testInitialize2() {
        //testing Initialize with 3 kwargs
        org.python.Object[] args = {};
        java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<>();
        kwargs.put("day", org.python.types.Int.getInt(30));
        kwargs.put("month", org.python.types.Int.getInt(9));
        kwargs.put("year", org.python.types.Int.getInt(2021));
        Date date = new Date(args, kwargs);
        assertEquals(new org.python.types.Str("30"), date.__day__());
        assertEquals(new org.python.types.Str("9"), date.__month__());
        assertEquals(new org.python.types.Str("2021"), date.__year__());
    }

    @Test
    public void testInitialize3() {
        //testing Initialize with 4 args
        org.python.Object[] args = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(30), org.python.types.Int.getInt(30)};
        java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<>();
        Exception exception = assertThrows(org.python.exceptions.TypeError.class, () -> {
            Date date = new Date(args, kwargs);
        });
    }

    @Test
    public void testInitialize4() {
        //testing Initialize with 3 args on leap year
        org.python.Object[] args = { org.python.types.Int.getInt(2020), org.python.types.Int.getInt(2), org.python.types.Int.getInt(29)};
        java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<>();

        assertDoesNotThrow(() -> new Date(args, kwargs));
    }

    @Test
    public void testInitialize5() {
        //testing Initialize with 3 args with a day after the 30th
        org.python.Object[] args = { org.python.types.Int.getInt(2020), org.python.types.Int.getInt(2), org.python.types.Int.getInt(42)};
        Exception exception = assertThrows(org.python.exceptions.ValueError.class, () -> new Date(args, Collections.emptyMap()));
        assertEquals("day is out of range for month", exception.getMessage());
    }

    @Test
    public void testInitialize6() {
        //testing Initialize with 2 args and 1 kwarg
        org.python.Object[] args = { org.python.types.Int.getInt(1), org.python.types.Int.getInt(1)};
        java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<>();
        kwargs.put("year", org.python.types.Int.getInt(1));
        Exception exception = assertThrows(org.python.exceptions.SyntaxError.class, () -> new Date(args, kwargs));
        assertEquals("positional argument follows keyword argument", exception.getMessage());
    }

    @Test
    public void testInitialize7() {
        //testing Initialize with 3 args with wrong datatype on the day
        org.python.Object[] args = { org.python.types.Int.getInt(1), org.python.types.Int.getInt(1), new org.python.types.Str("test")};
        Exception exception = assertThrows(org.python.exceptions.TypeError.class, () -> new Date(args, Collections.emptyMap()));
        assertEquals("integer argument expected, got str", exception.getMessage());
    }

    @Test
    public void testInitialize8() {
        ///testing Initialize with 2 args with wrong datatype on the year
        org.python.Object[] args = {new org.python.types.Str("test"), org.python.types.Int.getInt(1)};
        Exception exception = assertThrows(org.python.exceptions.TypeError.class, () -> new Date(args, Collections.emptyMap()));
        assertEquals("integer argument expected, got str", exception.getMessage());
    }

    @Test
    public void testInitialize9() {
        //testing Initialize with 2 args
        org.python.Object[] args = {org.python.types.Int.getInt(1), org.python.types.Int.getInt(1)};
        Exception exception = assertThrows(org.python.exceptions.TypeError.class, () -> new Date(args, Collections.emptyMap()));
        assertEquals("function missing required argument 'day' (pos 3)", exception.getMessage());
    }

    @Test
    public void testInitialize10() {
        //testing Initialize with 1 kwarg
        org.python.Object[] args = {};
        java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<>();
        kwargs.put("month", org.python.types.Int.getInt(1));
        Exception exception = assertThrows(org.python.exceptions.TypeError.class, () -> new Date(args, kwargs));
        assertEquals("function missing required argument 'year' (pos 1)", exception.getMessage());
    }

    @Test
    public void test__repr__() {
        org.python.Object[] args = { org.python.types.Int.getInt(1), org.python.types.Int.getInt(1), org.python.types.Int.getInt(1)};
        java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<>();
        Date date = new Date(args, kwargs);
        assertEquals("0001-01-01", date.__repr__().value);
    }

    @Test
    public void testToday() {
        java.time.LocalDateTime expected = java.time.LocalDateTime.now();
        Date date = (Date) Date.today();
        assertEquals(org.python.types.Int.getInt(expected.getYear()), date.year);
        assertEquals(org.python.types.Int.getInt(expected.getMonthValue()), date.month);
        assertEquals(org.python.types.Int.getInt(expected.getDayOfMonth()), date.day);
    }

    @Test
    public void testCTime() {
        org.python.Object[] args = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(15)};
        Date date = new Date(args, Collections.emptyMap());
        assertEquals(new org.python.types.Str("Wed Sep  15 00:00:00 2021"), date.ctime());
    }

    @Test
    public void testWeekday() {
        org.python.Object[] args = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(15)};
        Date date = new Date(args, Collections.emptyMap());
        assertEquals(2, new Integer(String.valueOf(date.weekday())));
    }

    @Test
    public void test__eq__(){
        org.python.Object[] args1 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date1 = new Date(args1, Collections.emptyMap());
        org.python.Object[] args2 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date2 = new Date(args2, Collections.emptyMap());
        org.python.Object[] args3 = { org.python.types.Int.getInt(2020), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date3 = new Date(args3, Collections.emptyMap());

        assertTrue(((org.python.types.Bool) date1.__eq__(date2)).value);
        assertFalse(((org.python.types.Bool) date1.__eq__(date3)).value);

        Exception exception = assertThrows(org.python.exceptions.TypeError.class,
            () -> date1.__eq__(new org.python.types.Str("test")));
        assertEquals("incompatible datatype(str)", exception.getMessage());
    }

    @Test
    public void test__ne__(){
        org.python.Object[] args1 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date1 = new Date(args1, Collections.emptyMap());
        org.python.Object[] args2 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date2 = new Date(args2, Collections.emptyMap());
        org.python.Object[] args3 = { org.python.types.Int.getInt(2020), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date3 = new Date(args3, Collections.emptyMap());

        assertTrue(((org.python.types.Bool) date1.__ne__(date3)).value);
        assertFalse(((org.python.types.Bool) date1.__ne__(date2)).value);

        Exception exception = assertThrows(org.python.exceptions.TypeError.class,
            () -> date1.__ne__(new org.python.types.Str("test")));
        assertEquals("incompatible datatype(str)", exception.getMessage());
    }

    @Test
    public void test__gt__(){
        org.python.Object[] args1 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date1 = new Date(args1, Collections.emptyMap());
        org.python.Object[] args2 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date2 = new Date(args2, Collections.emptyMap());
        org.python.Object[] args3 = { org.python.types.Int.getInt(2020), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date3 = new Date(args3, Collections.emptyMap());

        assertTrue(((org.python.types.Bool) date1.__gt__(date3)).value);
        assertFalse(((org.python.types.Bool) date1.__gt__(date2)).value);

        Exception exception = assertThrows(org.python.exceptions.TypeError.class,
            () -> date1.__gt__(new org.python.types.Str("test")));
        assertEquals("incompatible datatype(str)", exception.getMessage());
    }

    @Test
    public void test__lt__(){
        org.python.Object[] args1 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date1 = new Date(args1, Collections.emptyMap());
        org.python.Object[] args2 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date2 = new Date(args2, Collections.emptyMap());
        org.python.Object[] args3 = { org.python.types.Int.getInt(2020), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date3 = new Date(args3, Collections.emptyMap());

        assertTrue(((org.python.types.Bool) date3.__lt__(date1)).value);
        assertFalse(((org.python.types.Bool) date1.__lt__(date2)).value);

        Exception exception = assertThrows(org.python.exceptions.TypeError.class,
            () -> date1.__lt__(new org.python.types.Str("test")));
        assertEquals("incompatible datatype(str)", exception.getMessage());
    }

    @Test
    public void test__ge__(){
        org.python.Object[] args1 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date1 = new Date(args1, Collections.emptyMap());
        org.python.Object[] args2 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date2 = new Date(args2, Collections.emptyMap());
        org.python.Object[] args3 = { org.python.types.Int.getInt(2020), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date3 = new Date(args3, Collections.emptyMap());

        assertTrue(((org.python.types.Bool) date1.__ge__(date3)).value);
        assertFalse(((org.python.types.Bool) date3.__ge__(date1)).value);

        Exception exception = assertThrows(org.python.exceptions.TypeError.class,
            () -> date1.__ge__(new org.python.types.Str("test")));
        assertEquals("incompatible datatype(str)", exception.getMessage());
    }

    @Test
    public void test__le__(){
        org.python.Object[] args1 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date1 = new Date(args1, Collections.emptyMap());
        org.python.Object[] args2 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date2 = new Date(args2, Collections.emptyMap());
        org.python.Object[] args3 = { org.python.types.Int.getInt(2020), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date3 = new Date(args3, Collections.emptyMap());

        assertTrue(((org.python.types.Bool) date3.__le__(date1)).value);
        assertFalse(((org.python.types.Bool) date1.__le__(date3)).value);

        Exception exception = assertThrows(org.python.exceptions.TypeError.class,
            () -> date1.__le__(new org.python.types.Str("test")));
        assertEquals("incompatible datatype(str)", exception.getMessage());
    }

    @Test
    public void test_replace(){
        org.python.Object[] args1 = { org.python.types.Int.getInt(2021), org.python.types.Int.getInt(9), org.python.types.Int.getInt(19)};
        Date date1 = new Date(args1, Collections.emptyMap());

        java.util.Map<java.lang.String, org.python.Object> kwargs = new java.util.HashMap<>();
        kwargs.put("day", org.python.types.Int.getInt(30));

        org.python.Object[] args2 = {};
        assertEquals(new org.python.types.Str("2021-09-30"),date1.replace(kwargs).__repr__());
        Date date2 = new Date(args1, Collections.emptyMap());

        java.util.Map<java.lang.String, org.python.Object> kwargs2 = new java.util.HashMap<>();
        kwargs2.put("day", org.python.types.Int.getInt(50));

        Exception exception = assertThrows(org.python.exceptions.ValueError.class,
            () -> date2.replace(kwargs2));

        assertEquals("day is out of range for month", exception.getMessage());

        java.util.Map<java.lang.String, org.python.Object> kwargs3 = new java.util.HashMap<>();
        kwargs3.put("day", new org.python.types.Str("6"));

        Exception exception2 = assertThrows(org.python.exceptions.TypeError.class,
            () -> date2.replace(kwargs3));

        assertEquals("integer argument expected, got str", exception2.getMessage());
    }

    @Test
    public void test_fromisoformat(){

        org.python.types.Str str1 = new org.python.types.Str("2021-09-21");
        assertEquals(new org.python.types.Str("2021-09-21"), Date.fromisoformat(str1).__repr__());

        org.python.types.Str str2 = new org.python.types.Str("-200-12-01");
        Exception exception2 = assertThrows(org.python.exceptions.ValueError.class, () -> Date.fromisoformat(str2));
        assertEquals("Invalid string format", exception2.getMessage());
    }

}
