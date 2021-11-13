// Generated from /Users/gokul/Nok/Hackathon2021/CSGSO_BCBGSO_Fall_2021_Hackathon_Turing_Machine_Mechanics_of_Millennials/GokulFolder/eqSolver.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SOLVERLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, Identifier=7, Number=8, 
		Comment=9, WS=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "Identifier", "Number", 
			"Integer", "Float", "Sign", "Digit", "NonzeroDigit", "Letter", "Comment", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'='", "'+'", "'-'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "Identifier", "Number", "Comment", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public SOLVERLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "eqSolver.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\fn\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3"+
		"\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\7\b\63\n\b\f\b\16\b"+
		"\66\13\b\3\t\3\t\5\t:\n\t\3\n\5\n=\n\n\3\n\3\n\7\nA\n\n\f\n\16\nD\13\n"+
		"\3\n\5\nG\n\n\3\13\5\13J\n\13\3\13\6\13M\n\13\r\13\16\13N\3\13\3\13\6"+
		"\13S\n\13\r\13\16\13T\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\7"+
		"\20a\n\20\f\20\16\20d\13\20\3\20\3\20\3\21\6\21i\n\21\r\21\16\21j\3\21"+
		"\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\2\25\2\27\2\31\2\33"+
		"\2\35\2\37\13!\f\3\2\b\4\2--//\3\2\62;\3\2\63;\5\2C\\aac|\4\2\f\f\17\17"+
		"\5\2\13\f\17\17\"\"\2r\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2"+
		"\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\37\3\2\2\2\2!\3"+
		"\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2"+
		"\2\2\17/\3\2\2\2\219\3\2\2\2\23F\3\2\2\2\25I\3\2\2\2\27V\3\2\2\2\31X\3"+
		"\2\2\2\33Z\3\2\2\2\35\\\3\2\2\2\37^\3\2\2\2!h\3\2\2\2#$\7=\2\2$\4\3\2"+
		"\2\2%&\7?\2\2&\6\3\2\2\2\'(\7-\2\2(\b\3\2\2\2)*\7/\2\2*\n\3\2\2\2+,\7"+
		"*\2\2,\f\3\2\2\2-.\7+\2\2.\16\3\2\2\2/\64\5\35\17\2\60\63\5\35\17\2\61"+
		"\63\5\31\r\2\62\60\3\2\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64"+
		"\65\3\2\2\2\65\20\3\2\2\2\66\64\3\2\2\2\67:\5\23\n\28:\5\25\13\29\67\3"+
		"\2\2\298\3\2\2\2:\22\3\2\2\2;=\5\27\f\2<;\3\2\2\2<=\3\2\2\2=>\3\2\2\2"+
		">B\5\33\16\2?A\5\31\r\2@?\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CG\3\2"+
		"\2\2DB\3\2\2\2EG\7\62\2\2F<\3\2\2\2FE\3\2\2\2G\24\3\2\2\2HJ\5\27\f\2I"+
		"H\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KM\5\31\r\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2"+
		"NO\3\2\2\2OP\3\2\2\2PR\7\60\2\2QS\5\31\r\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2"+
		"\2TU\3\2\2\2U\26\3\2\2\2VW\t\2\2\2W\30\3\2\2\2XY\t\3\2\2Y\32\3\2\2\2Z"+
		"[\t\4\2\2[\34\3\2\2\2\\]\t\5\2\2]\36\3\2\2\2^b\7%\2\2_a\n\6\2\2`_\3\2"+
		"\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2db\3\2\2\2ef\b\20\2\2f \3"+
		"\2\2\2gi\t\7\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\b"+
		"\21\2\2m\"\3\2\2\2\16\2\62\649<BFINTbj\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}