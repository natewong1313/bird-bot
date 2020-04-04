__all__ = ['walmart_encryption']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['n', 'r', 'a', 'i', 'encrypt', 'o'])
@Js
def PyJsHoisted_encrypt_(e, t, PIE_L, PIE_E, PIE_K, PIE_key_id, PIE_phase, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'PIE_L':PIE_L, 'PIE_E':PIE_E, 'PIE_K':PIE_K, 'PIE_key_id':PIE_key_id, 'PIE_phase':PIE_phase, 'this':this, 'arguments':arguments}, var)
    var.registers(['PIE_L', 'PIE_K', 'l_var', 'PIE_key_id', 'p_var', 'i_var', 'PIE_E', 'u_var', 'PIE_phase', 'e', 'f_var', 'd_var', 'a_var', 't', 's_var', 'c_var'])
    var.put('PIE', Js({'L':var.get('parseInt')(var.get('PIE_L')),'E':var.get('parseInt')(var.get('PIE_E')),'K':var.get('PIE_K'),'key_id':var.get('PIE_key_id'),'phase':var.get('parseInt')(var.get('PIE_phase'))}))
    var.put('a_var', var.get('n').callprop('distill', var.get('e')))
    var.put('i_var', var.get('n').callprop('distill', var.get('t')))
    var.put('c_var', (var.get('a_var').callprop('substr', Js(0.0), var.get('PIE').get('L'))+var.get('a_var').callprop('substring', (var.get('a_var').get('length')-var.get('PIE').get('E')))))
    var.put('u_var', var.get('n').callprop('luhn', var.get('a_var')))
    var.put('s_var', var.get('a_var').callprop('substring', (var.get('PIE').get('L')+Js(1.0)), (var.get('a_var').get('length')-var.get('PIE').get('E'))))
    var.put('d_var', var.get('o').callprop('encrypt', (var.get('s_var')+var.get('i_var')), var.get('c_var'), var.get('PIE').get('K'), Js(10.0)))
    var.put('l_var', (((var.get('a_var').callprop('substr', Js(0.0), var.get('PIE').get('L'))+Js('0'))+var.get('d_var').callprop('substr', Js(0.0), (var.get('d_var').get('length')-var.get('i_var').get('length'))))+var.get('a_var').callprop('substring', (var.get('a_var').get('length')-var.get('PIE').get('E')))))
    var.put('f_var', var.get('n').callprop('reformat', var.get('n').callprop('fixluhn', var.get('l_var'), var.get('PIE').get('L'), var.get('u_var')), var.get('e')))
    var.put('p_var', var.get('n').callprop('reformat', var.get('d_var').callprop('substring', (var.get('d_var').get('length')-var.get('i_var').get('length'))), var.get('t')))
    return Js([var.get('f_var'), var.get('p_var'), var.get('n').callprop('integrity', var.get('PIE').get('K'), var.get('f_var'), var.get('p_var'))])
PyJsHoisted_encrypt_.func_name = 'encrypt'
var.put('encrypt', PyJsHoisted_encrypt_)
var.put('n', Js({}))
def PyJs_LONG_6_(var=var):
    @Js
    def PyJs_anonymous_0_(e, this, arguments, var=var):
        var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'n', 'e', 'r'])
        #for JS loop
        var.put('t', (var.get('e').get('length')-Js(1.0)))
        var.put('n', Js(0.0))
        while (var.get('t')>=Js(0.0)):
            PyJsComma(var.put('n', var.get('parseInt')(var.get('e').callprop('substr', var.get('t'), Js(1.0)), Js(10.0)), '+'),var.put('t', Js(2.0), '-'))
        
        #for JS loop
        var.put('t', (var.get('e').get('length')-Js(2.0)))
        while (var.get('t')>=Js(0.0)):
            var.put('r', (Js(2.0)*var.get('parseInt')(var.get('e').callprop('substr', var.get('t'), Js(1.0)), Js(10.0))))
            PyJsComma(var.put('n', (var.get('r') if (var.get('r')<Js(10.0)) else (var.get('r')-Js(9.0))), '+'),var.put('t', Js(2.0), '-'))
        
        return (var.get('n')%Js(10.0))
    PyJs_anonymous_0_._set_name('anonymous')
    @Js
    def PyJs_anonymous_1_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'e', 'a', 'r'])
        var.put('a', var.get('n').callprop('luhn', var.get('e')))
        def PyJs_LONG_2_(var=var):
            return (PyJsComma(var.put('a', ((Js(10.0)-var.get('a')) if (((var.get('e').get('length')-var.get('t'))%Js(2.0))!=Js(0.0)) else ((Js(5.0)-(var.get('a')/Js(2.0))) if ((var.get('a')%Js(2.0))==Js(0.0)) else (((Js(9.0)-var.get('a'))/Js(2.0))+Js(5.0))))),((var.get('e').callprop('substr', Js(0.0), var.get('t'))+var.get('a'))+var.get('e').callprop('substr', (var.get('t')+Js(1.0))))) if (Js(0.0)!=var.get('a')) else var.get('e'))
        return PyJsComma((var.put('a', (Js(10.0)-var.get('r')), '+') if (var.get('a')<var.get('r')) else var.put('a', var.get('r'), '-')),PyJs_LONG_2_())
    PyJs_anonymous_1_._set_name('anonymous')
    @Js
    def PyJs_anonymous_3_(e, this, arguments, var=var):
        var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'e', 'r'])
        #for JS loop
        var.put('t', Js(''))
        var.put('r', Js(0.0))
        while (var.get('r')<var.get('e').get('length')):
            try:
                ((var.get('n').get('base10').callprop('indexOf', var.get('e').callprop('charAt', var.get('r')))>=Js(0.0)) and var.put('t', var.get('e').callprop('substr', var.get('r'), Js(1.0)), '+'))
            finally:
                    var.put('r',Js(var.get('r').to_number())+Js(1))
        return var.get('t')
    PyJs_anonymous_3_._set_name('anonymous')
    @Js
    def PyJs_anonymous_4_(e, t, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'a', 'i', 'e', 't'])
        #for JS loop
        var.put('r', Js(''))
        var.put('a', Js(0.0))
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('t').get('length')):
            try:
                (PyJsComma(var.put('r', var.get('e').callprop('substr', var.get('a'), Js(1.0)), '+'),var.put('a',Js(var.get('a').to_number())+Js(1))) if ((var.get('a')<var.get('e').get('length')) and (var.get('n').get('base10').callprop('indexOf', var.get('t').callprop('charAt', var.get('i')))>=Js(0.0))) else var.put('r', var.get('t').callprop('substr', var.get('i'), Js(1.0)), '+'))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        return var.get('r')
    PyJs_anonymous_4_._set_name('anonymous')
    @Js
    def PyJs_anonymous_5_(e, t, n, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'c', 'u', 'e', 's', 't', 'o'])
        var.put('o', (((((var.get('String').callprop('fromCharCode', Js(0.0))+var.get('String').callprop('fromCharCode', var.get('t').get('length')))+var.get('t'))+var.get('String').callprop('fromCharCode', Js(0.0)))+var.get('String').callprop('fromCharCode', var.get('n').get('length')))+var.get('n')))
        var.put('c', var.get('a').callprop('HexToWords', var.get('e')))
        var.get('c').put('3', Js(1.0), '^')
        var.put('u', var.get('r').get('cipher').get('aes').create(var.get('c')))
        var.put('s', var.get('i').callprop('compute', var.get('u'), var.get('o')))
        return (var.get('a').callprop('WordToHex', var.get('s').get('0'))+var.get('a').callprop('WordToHex', var.get('s').get('1')))
    PyJs_anonymous_5_._set_name('anonymous')
    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('n').put('base10', Js('0123456789')),var.get('n').put('base62', Js('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))),var.get('n').put('luhn', PyJs_anonymous_0_)),var.get('n').put('fixluhn', PyJs_anonymous_1_)),var.get('n').put('distill', PyJs_anonymous_3_)),var.get('n').put('reformat', PyJs_anonymous_4_)),var.get('n').put('integrity', PyJs_anonymous_5_))
PyJs_LONG_6_()
@Js
def PyJs_anonymous_7_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    @Js
    def PyJs_anonymous_8_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (Js('CORRUPT: ')+var.get(u"this").get('message'))
    PyJs_anonymous_8_._set_name('anonymous')
    PyJsComma(var.get(u"this").put('toString', PyJs_anonymous_8_),var.get(u"this").put('message', var.get('e')))
PyJs_anonymous_7_._set_name('anonymous')
@Js
def PyJs_anonymous_9_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    @Js
    def PyJs_anonymous_10_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (Js('INVALID: ')+var.get(u"this").get('message'))
    PyJs_anonymous_10_._set_name('anonymous')
    PyJsComma(var.get(u"this").put('toString', PyJs_anonymous_10_),var.get(u"this").put('message', var.get('e')))
PyJs_anonymous_9_._set_name('anonymous')
@Js
def PyJs_anonymous_11_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    @Js
    def PyJs_anonymous_12_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (Js('BUG: ')+var.get(u"this").get('message'))
    PyJs_anonymous_12_._set_name('anonymous')
    PyJsComma(var.get(u"this").put('toString', PyJs_anonymous_12_),var.get(u"this").put('message', var.get('e')))
PyJs_anonymous_11_._set_name('anonymous')
var.put('r', Js({'cipher':Js({}),'hash':Js({}),'mode':Js({}),'misc':Js({}),'codec':Js({}),'exception':Js({'corrupt':PyJs_anonymous_7_,'invalid':PyJs_anonymous_9_,'bug':PyJs_anonymous_11_})}))
@Js
def PyJs_anonymous_13_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'd', 'c', 'a', 'u', 'i', 'e', 's', 't', 'o'])
    (var.get(u"this").get('_tables').get('0').get('0').get('0') or var.get(u"this").callprop('_precompute'))
    var.put('c', var.get(u"this").get('_tables').get('0').get('4'))
    var.put('u', var.get(u"this").get('_tables').get('1'))
    var.put('s', var.get('e').get('length'))
    var.put('d', Js(1.0))
    if ((PyJsStrictNeq(Js(4.0),var.get('s')) and PyJsStrictNeq(Js(6.0),var.get('s'))) and PyJsStrictNeq(Js(8.0),var.get('s'))):
        PyJsTempException = JsToPyException(var.get('r').get('exception').get('invalid').create(Js('invalid aes key size')))
        raise PyJsTempException
    #for JS loop
    PyJsComma(var.get(u"this").put('_key', Js([var.put('i', var.get('e').callprop('slice', Js(0.0))), var.put('o', Js([]))])),var.put('t', var.get('s')))
    while (var.get('t')<((Js(4.0)*var.get('s'))+Js(28.0))):
        try:
            def PyJs_LONG_14_(var=var):
                return PyJsComma(var.put('a', ((((var.get('c').get(PyJsBshift(var.get('a'),Js(24.0)))<<Js(24.0))^(var.get('c').get(((var.get('a')>>Js(16.0))&Js(255.0)))<<Js(16.0)))^(var.get('c').get(((var.get('a')>>Js(8.0))&Js(255.0)))<<Js(8.0)))^var.get('c').get((Js(255.0)&var.get('a'))))),(((var.get('t')%var.get('s'))==Js(0.0)) and PyJsComma(var.put('a', (((var.get('a')<<Js(8.0))^PyJsBshift(var.get('a'),Js(24.0)))^(var.get('d')<<Js(24.0)))),var.put('d', ((var.get('d')<<Js(1.0))^(Js(283.0)*(var.get('d')>>Js(7.0))))))))
            PyJsComma(PyJsComma(var.put('a', var.get('i').get((var.get('t')-Js(1.0)))),((((var.get('t')%var.get('s'))==Js(0.0)) or (PyJsStrictEq(Js(8.0),var.get('s')) and ((var.get('t')%var.get('s'))==Js(4.0)))) and PyJs_LONG_14_())),var.get('i').put(var.get('t'), (var.get('i').get((var.get('t')-var.get('s')))^var.get('a'))))
        finally:
                (var.put('t',Js(var.get('t').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('n', Js(0.0))
    while var.get('t'):
        try:
            def PyJs_LONG_15_(var=var):
                return var.get('o').put(var.get('n'), (var.get('a') if ((var.get('t')<=Js(4.0)) or (var.get('n')<Js(4.0))) else (((var.get('u').get('0').get(var.get('c').get(PyJsBshift(var.get('a'),Js(24.0))))^var.get('u').get('1').get(var.get('c').get(((var.get('a')>>Js(16.0))&Js(255.0)))))^var.get('u').get('2').get(var.get('c').get(((var.get('a')>>Js(8.0))&Js(255.0)))))^var.get('u').get('3').get(var.get('c').get((Js(255.0)&var.get('a')))))))
            PyJsComma(var.put('a', var.get('i').get((var.get('t') if (Js(3.0)&var.get('n')) else (var.get('t')-Js(4.0))))),PyJs_LONG_15_())
        finally:
                PyJsComma((var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1)),(var.put('t',Js(var.get('t').to_number())-Js(1))+Js(1)))
PyJs_anonymous_13_._set_name('anonymous')
@Js
def PyJs_anonymous_16_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get(u"this").callprop('_crypt', var.get('e'), Js(0.0))
PyJs_anonymous_16_._set_name('anonymous')
@Js
def PyJs_anonymous_17_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get(u"this").callprop('_crypt', var.get('e'), Js(1.0))
PyJs_anonymous_17_._set_name('anonymous')
@Js
def PyJs_anonymous_18_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'n', 'd', 'p', 'r', 'c', 'a', 'u', 'i', 'f', 'e', 's', 't', 'o'])
    var.put('u', var.get(u"this").get('_tables').get('0'))
    var.put('s', var.get(u"this").get('_tables').get('1'))
    var.put('d', var.get('u').get('4'))
    var.put('l', var.get('s').get('4'))
    var.put('f', Js([]))
    var.put('p', Js([]))
    #for JS loop
    var.put('e', Js(0.0))
    while (var.get('e')<Js(256.0)):
        try:
            var.get('p').put((var.get('f').put(var.get('e'), ((var.get('e')<<Js(1.0))^(Js(283.0)*(var.get('e')>>Js(7.0)))))^var.get('e')), var.get('e'))
        finally:
                (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('t', var.put('n', Js(0.0)))
    while var.get('d').get(var.get('t')).neg():
        try:
            #for JS loop
            def PyJs_LONG_19_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('i', (((var.put('i', ((((var.get('n')^(var.get('n')<<Js(1.0)))^(var.get('n')<<Js(2.0)))^(var.get('n')<<Js(3.0)))^(var.get('n')<<Js(4.0))))>>Js(8.0))^(Js(255.0)&var.get('i')))^Js(99.0))),var.get('d').put(var.get('t'), var.get('i'))),var.get('l').put(var.get('i'), var.get('t'))),var.put('c', ((((Js(16843009.0)*var.get('f').get(var.put('a', var.get('f').get(var.put('r', var.get('f').get(var.get('t')))))))^(Js(65537.0)*var.get('a')))^(Js(257.0)*var.get('r')))^(Js(16843008.0)*var.get('t'))))),var.put('o', ((Js(257.0)*var.get('f').get(var.get('i')))^(Js(16843008.0)*var.get('i'))))),var.put('e', Js(0.0)))
            PyJs_LONG_19_()
            while (var.get('e')<Js(4.0)):
                try:
                    PyJsComma(var.get('u').get(var.get('e')).put(var.get('t'), var.put('o', ((var.get('o')<<Js(24.0))^PyJsBshift(var.get('o'),Js(8.0))))),var.get('s').get(var.get('e')).put(var.get('i'), var.put('c', ((var.get('c')<<Js(24.0))^PyJsBshift(var.get('c'),Js(8.0))))))
                finally:
                        (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
        finally:
                PyJsComma(var.put('t', (Js(1.0) if (Js(0.0)==var.get('r')) else var.get('r')), '^'),var.put('n', (Js(1.0) if (Js(0.0)==var.get('p').get(var.get('n'))) else var.get('p').get(var.get('n')))))
    #for JS loop
    var.put('e', Js(0.0))
    while (var.get('e')<Js(5.0)):
        try:
            PyJsComma(var.get('u').put(var.get('e'), var.get('u').get(var.get('e')).callprop('slice', Js(0.0))),var.get('s').put(var.get('e'), var.get('s').get(var.get('e')).callprop('slice', Js(0.0))))
        finally:
                (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
PyJs_anonymous_18_._set_name('anonymous')
@Js
def PyJs_anonymous_20_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'n', 'd', 'p', 'y', 'c', 'b', 'a', 'u', 'i', 'f', 'm', 'h', 'v', 'e', 's', 't', 'g', 'o', 'E'])
    if PyJsStrictNeq(Js(4.0),var.get('e').get('length')):
        PyJsTempException = JsToPyException(var.get('r').get('exception').get('invalid').create(Js('invalid aes block size')))
        raise PyJsTempException
    var.put('c', var.get(u"this").get('_key').get(var.get('t')))
    var.put('u', (var.get('e').get('0')^var.get('c').get('0')))
    var.put('s', (var.get('e').get((Js(3.0) if var.get('t') else Js(1.0)))^var.get('c').get('1')))
    var.put('d', (var.get('e').get('2')^var.get('c').get('2')))
    var.put('l', (var.get('e').get((Js(1.0) if var.get('t') else Js(3.0)))^var.get('c').get('3')))
    var.put('f', ((var.get('c').get('length')/Js(4.0))-Js(2.0)))
    var.put('p', Js(4.0))
    var.put('m', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('h', var.get(u"this").get('_tables').get(var.get('t')))
    var.put('b', var.get('h').get('0'))
    var.put('v', var.get('h').get('1'))
    var.put('y', var.get('h').get('2'))
    var.put('E', var.get('h').get('3'))
    var.put('g', var.get('h').get('4'))
    #for JS loop
    var.put('o', Js(0.0))
    while (var.get('o')<var.get('f')):
        try:
            def PyJs_LONG_21_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('n', ((((var.get('b').get(PyJsBshift(var.get('u'),Js(24.0)))^var.get('v').get(((var.get('s')>>Js(16.0))&Js(255.0))))^var.get('y').get(((var.get('d')>>Js(8.0))&Js(255.0))))^var.get('E').get((Js(255.0)&var.get('l'))))^var.get('c').get(var.get('p')))),var.put('a', ((((var.get('b').get(PyJsBshift(var.get('s'),Js(24.0)))^var.get('v').get(((var.get('d')>>Js(16.0))&Js(255.0))))^var.get('y').get(((var.get('l')>>Js(8.0))&Js(255.0))))^var.get('E').get((Js(255.0)&var.get('u'))))^var.get('c').get((var.get('p')+Js(1.0)))))),var.put('i', ((((var.get('b').get(PyJsBshift(var.get('d'),Js(24.0)))^var.get('v').get(((var.get('l')>>Js(16.0))&Js(255.0))))^var.get('y').get(((var.get('u')>>Js(8.0))&Js(255.0))))^var.get('E').get((Js(255.0)&var.get('s'))))^var.get('c').get((var.get('p')+Js(2.0)))))),var.put('l', ((((var.get('b').get(PyJsBshift(var.get('l'),Js(24.0)))^var.get('v').get(((var.get('u')>>Js(16.0))&Js(255.0))))^var.get('y').get(((var.get('s')>>Js(8.0))&Js(255.0))))^var.get('E').get((Js(255.0)&var.get('d'))))^var.get('c').get((var.get('p')+Js(3.0)))))),var.put('p', Js(4.0), '+')),var.put('u', var.get('n'))),var.put('s', var.get('a'))),var.put('d', var.get('i')))
            PyJs_LONG_21_()
        finally:
                (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('o', Js(0.0))
    while (var.get('o')<Js(4.0)):
        try:
            def PyJs_LONG_22_(var=var):
                return var.get('m').put(((Js(3.0)&(-var.get('o'))) if var.get('t') else var.get('o')), (((((var.get('g').get(PyJsBshift(var.get('u'),Js(24.0)))<<Js(24.0))^(var.get('g').get(((var.get('s')>>Js(16.0))&Js(255.0)))<<Js(16.0)))^(var.get('g').get(((var.get('d')>>Js(8.0))&Js(255.0)))<<Js(8.0)))^var.get('g').get((Js(255.0)&var.get('l'))))^var.get('c').get((var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1)))))
            PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJs_LONG_22_(),var.put('n', var.get('u'))),var.put('u', var.get('s'))),var.put('s', var.get('d'))),var.put('d', var.get('l'))),var.put('l', var.get('n')))
        finally:
                (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
    return var.get('m')
PyJs_anonymous_20_._set_name('anonymous')
PyJsComma(var.get('r').get('cipher').put('aes', PyJs_anonymous_13_),var.get('r').get('cipher').get('aes').put('prototype', Js({'encrypt':PyJs_anonymous_16_,'decrypt':PyJs_anonymous_17_,'_tables':Js([Js([Js([]), Js([]), Js([]), Js([]), Js([])]), Js([Js([]), Js([]), Js([]), Js([]), Js([])])]),'_precompute':PyJs_anonymous_18_,'_crypt':PyJs_anonymous_20_})))
@Js
def PyJs_anonymous_23_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return var.get('r').get('cipher').get('aes').create(var.get('a').callprop('HexToWords', var.get('e')))
PyJs_anonymous_23_._set_name('anonymous')
@Js
def PyJs_anonymous_24_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'n', 'e'])
    var.put('t', var.get('Array').create(Js(4.0)))
    if (Js(32.0)!=var.get('e').get('length')):
        return var.get(u"null")
    #for JS loop
    var.put('n', Js(0.0))
    while (var.get('n')<Js(4.0)):
        try:
            var.get('t').put(var.get('n'), var.get('parseInt')(var.get('e').callprop('substr', (Js(8.0)*var.get('n')), Js(8.0)), Js(16.0)))
        finally:
                (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
    return var.get('t')
PyJs_anonymous_24_._set_name('anonymous')
@Js
def PyJs_anonymous_25_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'n', 'e'])
    #for JS loop
    var.put('t', Js(32.0))
    var.put('n', Js(''))
    while (var.get('t')>Js(0.0)):
        PyJsComma(var.put('t', Js(4.0), '-'),var.put('n', var.get('a').get('Hex').callprop('substr', (PyJsBshift(var.get('e'),var.get('t'))&Js(15.0)), Js(1.0)), '+'))
    
    return var.get('n')
PyJs_anonymous_25_._set_name('anonymous')
var.put('a', Js({'HexToKey':PyJs_anonymous_23_,'HexToWords':PyJs_anonymous_24_,'Hex':Js('0123456789abcdef'),'WordToHex':PyJs_anonymous_25_}))
var.put('i', Js({}))
@Js
def PyJs_anonymous_26_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    return (Js(2147483647.0)!=(Js(2147483647.0)|var.get('e')))
PyJs_anonymous_26_._set_name('anonymous')
@Js
def PyJs_anonymous_27_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e'])
    def PyJs_LONG_28_(var=var):
        return PyJsComma(PyJsComma(PyJsComma(var.get('e').put('0', (((Js(2147483647.0)&var.get('e').get('0'))<<Js(1.0))|PyJsBshift(var.get('e').get('1'),Js(31.0)))),var.get('e').put('1', (((Js(2147483647.0)&var.get('e').get('1'))<<Js(1.0))|PyJsBshift(var.get('e').get('2'),Js(31.0))))),var.get('e').put('2', (((Js(2147483647.0)&var.get('e').get('2'))<<Js(1.0))|PyJsBshift(var.get('e').get('3'),Js(31.0))))),var.get('e').put('3', ((Js(2147483647.0)&var.get('e').get('3'))<<Js(1.0))))
    PyJs_LONG_28_()
PyJs_anonymous_27_._set_name('anonymous')
@Js
def PyJs_anonymous_29_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'r', 'a', 'e', 't', 'o'])
    var.put('n', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('r', var.get('e').callprop('encrypt', var.get('n')))
    var.put('a', var.get('r').get('0'))
    PyJsComma(var.get('i').callprop('leftShift', var.get('r')),(var.get('i').callprop('MSBnotZero', var.get('a')) and var.get('r').put('3', var.get('i').get('const_Rb'), '^')))
    #for JS loop
    var.put('o', Js(0.0))
    while (var.get('o')<var.get('t').get('length')):
        PyJsComma(var.get('n').put(((var.get('o')>>Js(2.0))&Js(3.0)), ((Js(255.0)&var.get('t').callprop('charCodeAt', var.get('o')))<<(Js(8.0)*(Js(3.0)-(Js(3.0)&var.get('o'))))), '^'),(((Js(0.0)==(Js(15.0)&var.put('o',Js(var.get('o').to_number())+Js(1)))) and (var.get('o')<var.get('t').get('length'))) and var.put('n', var.get('e').callprop('encrypt', var.get('n')))))
    
    def PyJs_LONG_30_(var=var):
        return (((Js(0.0)!=var.get('o')) and (Js(0.0)==(Js(15.0)&var.get('o')))) or PyJsComma(PyJsComma(PyJsComma(var.put('a', var.get('r').get('0')),var.get('i').callprop('leftShift', var.get('r'))),(var.get('i').callprop('MSBnotZero', var.get('a')) and var.get('r').put('3', var.get('i').get('const_Rb'), '^'))),var.get('n').put(((var.get('o')>>Js(2.0))&Js(3.0)), (Js(128.0)<<(Js(8.0)*(Js(3.0)-(Js(3.0)&var.get('o'))))), '^')))
    return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJs_LONG_30_(),var.get('n').put('0', var.get('r').get('0'), '^')),var.get('n').put('1', var.get('r').get('1'), '^')),var.get('n').put('2', var.get('r').get('2'), '^')),var.get('n').put('3', var.get('r').get('3'), '^')),var.get('e').callprop('encrypt', var.get('n')))
PyJs_anonymous_29_._set_name('anonymous')
PyJsComma(PyJsComma(PyJsComma(var.get('i').put('MSBnotZero', PyJs_anonymous_26_),var.get('i').put('leftShift', PyJs_anonymous_27_)),var.get('i').put('const_Rb', Js(135.0))),var.get('i').put('compute', PyJs_anonymous_29_))
@Js
def PyJs_anonymous_31_(e, t, n, r, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'r', 'a', 'i', 'e', 't'])
    var.put('a', var.get('Array').create(Js(4.0)))
    var.put('i', var.get('n').get('length'))
    def PyJs_LONG_32_(var=var):
        return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('a').put('0', (Js(16908544.0)|((var.get('r')>>Js(16.0))&Js(255.0)))),var.get('a').put('1', ((((((var.get('r')>>Js(8.0))&Js(255.0))<<Js(24.0))|((Js(255.0)&var.get('r'))<<Js(16.0)))|Js(2560.0))|(Js(255.0)&var.get('Math').callprop('floor', (var.get('t')/Js(2.0))))))),var.get('a').put('2', var.get('t'))),var.get('a').put('3', var.get('i'))),var.get('e').callprop('encrypt', var.get('a')))
    return PyJs_LONG_32_()
PyJs_anonymous_31_._set_name('anonymous')
@Js
def PyJs_anonymous_33_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'r', 'a', 'e', 't'])
    #for JS loop
    var.put('n', var.get('Math').callprop('ceil', (var.get('t')/Js(2.0))))
    var.put('r', Js(0.0))
    var.put('a', Js(1.0))
    while (var.get('n')>Js(0.0)):
        PyJsComma(var.put('n',Js(var.get('n').to_number())-Js(1)),((var.put('a', var.get('e'), '*')>=Js(256.0)) and PyJsComma(var.put('a', Js(256.0), '/'),var.put('r',Js(var.get('r').to_number())+Js(1)))))
    
    return PyJsComma(((var.get('a')>Js(1.0)) and var.put('r',Js(var.get('r').to_number())+Js(1))),var.get('r'))
PyJs_anonymous_33_._set_name('anonymous')
@Js
def PyJs_anonymous_34_(e, t, n, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'r', 'a', 'i', 'e', 't'])
    var.put('a', Js(0.0))
    #for JS loop
    var.put('r', (var.get('e').get('length')-Js(1.0)))
    while (var.get('r')>=Js(0.0)):
        try:
            var.put('i', ((var.get('e').get(var.get('r'))*var.get('n'))+var.get('a')))
            PyJsComma(var.get('e').put(var.get('r'), (var.get('i')%var.get('t'))),var.put('a', ((var.get('i')-var.get('e').get(var.get('r')))/var.get('t'))))
        finally:
                var.put('r',Js(var.get('r').to_number())-Js(1))
PyJs_anonymous_34_._set_name('anonymous')
@Js
def PyJs_anonymous_35_(e, t, n, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'r', 'a', 'i', 'e', 't'])
    #for JS loop
    var.put('r', (var.get('e').get('length')-Js(1.0)))
    var.put('a', var.get('n'))
    while ((var.get('r')>=Js(0.0)) and (var.get('a')>Js(0.0))):
        var.put('i', (var.get('e').get(var.get('r'))+var.get('a')))
        PyJsComma(PyJsComma(var.get('e').put(var.get('r'), (var.get('i')%var.get('t'))),var.put('a', ((var.get('i')-var.get('e').get(var.get('r')))/var.get('t')))),var.put('r',Js(var.get('r').to_number())-Js(1)))
    
PyJs_anonymous_35_._set_name('anonymous')
@Js
def PyJs_anonymous_36_(e, t, n, r, a, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'r', 'c', 'a', 'u', 'i', 'e', 't'])
    var.put('c', var.get('Array').create(var.get('r')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('r')):
        try:
            var.get('c').put(var.get('i'), Js(0.0))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    #for JS loop
    var.put('u', Js(0.0))
    while (var.get('u')<var.get('t')):
        try:
            PyJsComma(var.get('o').callprop('bnMultiply', var.get('c'), var.get('a'), var.get('n')),var.get('o').callprop('bnAdd', var.get('c'), var.get('a'), var.get('e').get(var.get('u'))))
        finally:
                var.put('u',Js(var.get('u').to_number())+Js(1))
    return var.get('c')
PyJs_anonymous_36_._set_name('anonymous')
@Js
def PyJs_anonymous_37_(e, t, n, r, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'r', 'a', 'i', 'e', 't', 'o'])
    #for JS loop
    var.put('a', var.get('Array').create(Js(4.0)))
    var.put('i', Js(0.0))
    while (var.get('i')<Js(4.0)):
        try:
            var.get('a').put(var.get('i'), var.get('e').get(var.get('i')))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    #for JS loop
    var.put('o', Js(0.0))
    while ((Js(4.0)*var.get('o'))<var.get('n')):
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<Js(4.0)):
            try:
                var.get('a').put(var.get('i'), (var.get('a').get(var.get('i'))^((((var.get('t').get((Js(4.0)*(var.get('o')+var.get('i'))))<<Js(24.0))|(var.get('t').get(((Js(4.0)*(var.get('o')+var.get('i')))+Js(1.0)))<<Js(16.0)))|(var.get('t').get(((Js(4.0)*(var.get('o')+var.get('i')))+Js(2.0)))<<Js(8.0)))|var.get('t').get(((Js(4.0)*(var.get('o')+var.get('i')))+Js(3.0))))))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        PyJsComma(var.put('a', var.get('r').callprop('encrypt', var.get('a'))),var.put('o', Js(4.0), '+'))
    
    return var.get('a')
PyJs_anonymous_37_._set_name('anonymous')
@Js
def PyJs_anonymous_38_(e, t, n, r, a, i, c, u, s, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'r':r, 'a':a, 'i':i, 'c':c, 'u':u, 's':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'n', 'd', 'p', 'y', 'r', 'c', 'b', 'm', 'a', 'i', 'h', 'u', 'v', 'e', 's', 't', 'f', 'E'])
    var.put('d', (var.get('Math').callprop('ceil', (var.get('s')/Js(4.0)))+Js(1.0)))
    var.put('l', (((var.get('n').get('length')+var.get('s'))+Js(1.0))&Js(15.0)))
    ((var.get('l')>Js(0.0)) and var.put('l', (Js(16.0)-var.get('l'))))
    var.put('p', var.get('Array').create((((var.get('n').get('length')+var.get('l'))+var.get('s'))+Js(1.0))))
    #for JS loop
    var.put('f', Js(0.0))
    while (var.get('f')<var.get('n').get('length')):
        try:
            var.get('p').put(var.get('f'), var.get('n').callprop('charCodeAt', var.get('f')))
        finally:
                (var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1))
    #for JS loop
    
    while (var.get('f')<(var.get('l')+var.get('n').get('length'))):
        try:
            var.get('p').put(var.get('f'), Js(0.0))
        finally:
                (var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1))
    var.get('p').put(((var.get('p').get('length')-var.get('s'))-Js(1.0)), var.get('t'))
    #for JS loop
    var.put('m', var.get('o').callprop('convertRadix', var.get('r'), var.get('a'), var.get('u'), var.get('s'), Js(256.0)))
    var.put('h', Js(0.0))
    while (var.get('h')<var.get('s')):
        try:
            var.get('p').put(((var.get('p').get('length')-var.get('s'))+var.get('h')), var.get('m').get(var.get('h')))
        finally:
                (var.put('h',Js(var.get('h').to_number())+Js(1))-Js(1))
    var.put('v', var.get('o').callprop('cbcmacq', var.get('c'), var.get('p'), var.get('p').get('length'), var.get('e')))
    var.put('y', var.get('v'))
    var.put('E', var.get('Array').create((Js(2.0)*var.get('d'))))
    #for JS loop
    var.put('f', Js(0.0))
    while (var.get('f')<var.get('d')):
        try:
            def PyJs_LONG_39_(var=var):
                return (((var.get('f')>Js(0.0)) and (Js(0.0)==(Js(3.0)&var.get('f')))) and PyJsComma(PyJsComma(var.put('b', ((var.get('f')>>Js(2.0))&Js(255.0))),var.put('b', (((var.get('b')<<Js(8.0))|(var.get('b')<<Js(16.0)))|(var.get('b')<<Js(24.0))), '|')),var.put('y', var.get('e').callprop('encrypt', Js([(var.get('v').get('0')^var.get('b')), (var.get('v').get('1')^var.get('b')), (var.get('v').get('2')^var.get('b')), (var.get('v').get('3')^var.get('b'))])))))
            PyJsComma(PyJsComma(PyJs_LONG_39_(),var.get('E').put((Js(2.0)*var.get('f')), PyJsBshift(var.get('y').get((Js(3.0)&var.get('f'))),Js(16.0)))),var.get('E').put(((Js(2.0)*var.get('f'))+Js(1.0)), (Js(65535.0)&var.get('y').get((Js(3.0)&var.get('f'))))))
        finally:
                var.put('f',Js(var.get('f').to_number())+Js(1))
    return var.get('o').callprop('convertRadix', var.get('E'), (Js(2.0)*var.get('d')), Js(65536.0), var.get('i'), var.get('u'))
PyJs_anonymous_38_._set_name('anonymous')
@Js
def PyJs_anonymous_40_(e, t, n, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'r', 'a', 'i', 'e', 't', 'o'])
    var.put('r', var.get('Array').create(var.get('t')))
    if (Js(256.0)==var.get('n')):
        #for JS loop
        var.put('a', Js(0.0))
        while (var.get('a')<var.get('t')):
            try:
                var.get('r').put(var.get('a'), var.get('e').callprop('charCodeAt', var.get('a')))
            finally:
                    (var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))
        return var.get('r')
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('t')):
        try:
            var.put('o', var.get('parseInt')(var.get('e').callprop('charAt', var.get('i')), var.get('n')))
            if ((var.get('NaN')==var.get('o')) or (var.get('o')<var.get('n')).neg()):
                return Js('')
            var.get('r').put(var.get('i'), var.get('o'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('r')
PyJs_anonymous_40_._set_name('anonymous')
@Js
def PyJs_anonymous_41_(e, t, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 'n', 'e', 'r'])
    var.put('r', Js(''))
    if (Js(256.0)==var.get('t')):
        #for JS loop
        var.put('n', Js(0.0))
        while (var.get('n')<var.get('e').get('length')):
            try:
                var.put('r', var.get('String').callprop('fromCharCode', var.get('e').get(var.get('n'))), '+')
            finally:
                    (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
    else:
        #for JS loop
        var.put('n', Js(0.0))
        while (var.get('n')<var.get('e').get('length')):
            try:
                var.put('r', var.get('o').get('alphabet').get(var.get('e').get(var.get('n'))), '+')
            finally:
                    (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
    return var.get('r')
PyJs_anonymous_41_._set_name('anonymous')
@Js
def PyJs_anonymous_42_(e, t, n, r, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
    var.registers(['l', 'n', 'd', 'p', 'r', 'c', 'a', 'u', 'i', 'm', 'h', 'e', 's', 't', 'f'])
    var.put('a', var.get('e').get('length'))
    var.put('i', var.get('Math').callprop('floor', (var.get('a')/Js(2.0))))
    var.put('c', var.get('o').callprop('precompF', var.get('n'), var.get('a'), var.get('t'), var.get('r')))
    var.put('u', var.get('o').callprop('precompb', var.get('r'), var.get('a')))
    var.put('s', var.get('o').callprop('DigitToVal', var.get('e'), var.get('i'), var.get('r')))
    var.put('d', var.get('o').callprop('DigitToVal', var.get('e').callprop('substr', var.get('i')), (var.get('a')-var.get('i')), var.get('r')))
    if ((Js('')==var.get('s')) or (Js('')==var.get('d'))):
        return Js('')
    #for JS loop
    var.put('l', Js(0.0))
    while (var.get('l')<Js(5.0)):
        try:
            var.put('p', var.get('o').callprop('F', var.get('n'), (Js(2.0)*var.get('l')), var.get('t'), var.get('d'), var.get('d').get('length'), var.get('s').get('length'), var.get('c'), var.get('r'), var.get('u')))
            var.put('f', Js(0.0))
            #for JS loop
            var.put('m', (var.get('s').get('length')-Js(1.0)))
            while (var.get('m')>=Js(0.0)):
                try:
                    (PyJsComma(var.get('s').put(var.get('m'), var.get('h')),var.put('f', Js(0.0))) if (var.put('h', ((var.get('s').get(var.get('m'))+var.get('p').get(var.get('m')))+var.get('f')))<var.get('r')) else PyJsComma(var.get('s').put(var.get('m'), (var.get('h')-var.get('r'))),var.put('f', Js(1.0))))
                finally:
                        var.put('m',Js(var.get('m').to_number())-Js(1))
            var.put('p', var.get('o').callprop('F', var.get('n'), ((Js(2.0)*var.get('l'))+Js(1.0)), var.get('t'), var.get('s'), var.get('s').get('length'), var.get('d').get('length'), var.get('c'), var.get('r'), var.get('u')))
            var.put('f', Js(0.0))
            #for JS loop
            var.put('m', (var.get('d').get('length')-Js(1.0)))
            while (var.get('m')>=Js(0.0)):
                try:
                    pass
                    (PyJsComma(var.get('d').put(var.get('m'), var.get('h')),var.put('f', Js(0.0))) if (var.put('h', ((var.get('d').get(var.get('m'))+var.get('p').get(var.get('m')))+var.get('f')))<var.get('r')) else PyJsComma(var.get('d').put(var.get('m'), (var.get('h')-var.get('r'))),var.put('f', Js(1.0))))
                finally:
                        var.put('m',Js(var.get('m').to_number())-Js(1))
        finally:
                (var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))
    return (var.get('o').callprop('ValToDigit', var.get('s'), var.get('r'))+var.get('o').callprop('ValToDigit', var.get('d'), var.get('r')))
PyJs_anonymous_42_._set_name('anonymous')
@Js
def PyJs_anonymous_43_(e, t, n, r, this, arguments, var=var):
    var = Scope({'e':e, 't':t, 'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'r', 'i', 'e', 't'])
    var.put('i', var.get('a').callprop('HexToKey', var.get('n')))
    return (Js('') if (var.get(u"null")==var.get('i')) else var.get('o').callprop('encryptWithCipher', var.get('e'), var.get('t'), var.get('i'), var.get('r')))
PyJs_anonymous_43_._set_name('anonymous')
var.put('o', Js({'alphabet':Js([Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z')]),'precompF':PyJs_anonymous_31_,'precompb':PyJs_anonymous_33_,'bnMultiply':PyJs_anonymous_34_,'bnAdd':PyJs_anonymous_35_,'convertRadix':PyJs_anonymous_36_,'cbcmacq':PyJs_anonymous_37_,'F':PyJs_anonymous_38_,'DigitToVal':PyJs_anonymous_40_,'ValToDigit':PyJs_anonymous_41_,'encryptWithCipher':PyJs_anonymous_42_,'encrypt':PyJs_anonymous_43_}))
pass
pass


# Add lib to the module scope
walmart_encryption = var.to_python()