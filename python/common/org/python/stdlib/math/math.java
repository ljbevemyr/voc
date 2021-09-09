package python;

@org.python.Module(
        __doc__ =
                "TODO"
)
public class math extends org.python.types.Module {
    public math() {
        super();
    }

    public static org.python.Object _STRUCT_TM_ITEMS;

    @org.python.Attribute
    public static org.python.Object __file__ = new org.python.types.Str("python/common/python/math.java");

    @org.python.Method(
         __doc__ = "Return the square root of number",
        args ={"number"}
    )
    public static org.python.Object sqrt(org.python.Object number) {
        if (number instanceof org.python.types.Float){
            if(((org.python.types.Float) number).value < 0.0){
                throw new org.python.exceptions.ValueError("math domain error");
            }
            return new org.python.types.Float(Math.sqrt(((org.python.types.Float) number.__float__()).value));
        }
        else if(number instanceof org.python.types.Int){
            if(((org.python.types.Int) number).value < 0){
                throw new org.python.exceptions.ValueError("math domain error");
            }
            return new org.python.types.Float(Math.sqrt(((org.python.types.Float) number.__float__()).value));
        }
        else if(number instanceof org.python.types.Bool) {
            boolean val = ((org.python.types.Bool) number).value;
            return new org.python.types.Float(val ? 1 : 0);
        }
        else{
            throw new org.python.exceptions.TypeError("floor() argument must be real number, not "+ number.typeName());
        }
        
    }

}
