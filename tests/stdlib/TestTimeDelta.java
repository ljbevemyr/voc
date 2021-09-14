import org.python.stdlib.datetime;
import junit.extensions.TestSetup;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

public class TestTimeDelta extends TestCase {

    public static Test suite() {
        TestSetup setup = new TestSetup(new TestSuite(TestTimeDelta.class)) {
            protected void setUp() throws Exception {
                // do your one-time setup here!
            }

            protected void tearDown() throws Exception {
                // do your one-time tear down here!
            }
        };
        return setup;
    }

    public void testTrue() {
        assertTrue(true);
    }
}