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
public class eqSolverLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, Identifier=6, Number=7, Comment=8, 
		WS=9, NEWLINE=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "Identifier", "Number", "Integer", 
			"Float", "Sign", "Digit", "NonzeroDigit", "Letter", "Comment", "WS", 
			"NEWLINE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'+'", "'-'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "Identifier", "Number", "Comment", 
			"WS", "NEWLINE"
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


	public eqSolverLexer(CharStream input) {
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\fq\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3"+
		"\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7\64\n\7\3\b"+
		"\3\b\5\b8\n\b\3\t\5\t;\n\t\3\t\3\t\7\t?\n\t\f\t\16\tB\13\t\3\t\5\tE\n"+
		"\t\3\n\5\nH\n\n\3\n\6\nK\n\n\r\n\16\nL\3\n\3\n\6\nQ\n\n\r\n\16\nR\3\13"+
		"\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\7\17_\n\17\f\17\16\17b\13\17"+
		"\3\17\3\17\3\20\6\20g\n\20\r\20\16\20h\3\20\3\20\3\21\5\21n\n\21\3\21"+
		"\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\2\23\2\25\2\27\2\31\2\33"+
		"\2\35\n\37\13!\f\3\2\b\4\2--//\3\2\62;\3\2\63;\5\2C\\aac|\4\2\f\f\17\17"+
		"\5\2\13\13\17\17\"\"\2u\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!"+
		"\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r\63"+
		"\3\2\2\2\17\67\3\2\2\2\21D\3\2\2\2\23G\3\2\2\2\25T\3\2\2\2\27V\3\2\2\2"+
		"\31X\3\2\2\2\33Z\3\2\2\2\35\\\3\2\2\2\37f\3\2\2\2!m\3\2\2\2#$\7?\2\2$"+
		"\4\3\2\2\2%&\7-\2\2&\6\3\2\2\2\'(\7/\2\2(\b\3\2\2\2)*\7*\2\2*\n\3\2\2"+
		"\2+,\7+\2\2,\f\3\2\2\2-.\5\33\16\2./\5\17\b\2/\64\3\2\2\2\60\61\5\17\b"+
		"\2\61\62\5\33\16\2\62\64\3\2\2\2\63-\3\2\2\2\63\60\3\2\2\2\64\16\3\2\2"+
		"\2\658\5\21\t\2\668\5\23\n\2\67\65\3\2\2\2\67\66\3\2\2\28\20\3\2\2\29"+
		";\5\25\13\2:9\3\2\2\2:;\3\2\2\2;<\3\2\2\2<@\5\31\r\2=?\5\27\f\2>=\3\2"+
		"\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2AE\3\2\2\2B@\3\2\2\2CE\7\62\2\2D:\3"+
		"\2\2\2DC\3\2\2\2E\22\3\2\2\2FH\5\25\13\2GF\3\2\2\2GH\3\2\2\2HJ\3\2\2\2"+
		"IK\5\27\f\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MN\3\2\2\2NP\7\60\2"+
		"\2OQ\5\27\f\2PO\3\2\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\24\3\2\2\2TU\t"+
		"\2\2\2U\26\3\2\2\2VW\t\3\2\2W\30\3\2\2\2XY\t\4\2\2Y\32\3\2\2\2Z[\t\5\2"+
		"\2[\34\3\2\2\2\\`\7%\2\2]_\n\6\2\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2"+
		"\2\2ac\3\2\2\2b`\3\2\2\2cd\b\17\2\2d\36\3\2\2\2eg\t\7\2\2fe\3\2\2\2gh"+
		"\3\2\2\2hf\3\2\2\2hi\3\2\2\2ij\3\2\2\2jk\b\20\2\2k \3\2\2\2ln\7\17\2\2"+
		"ml\3\2\2\2mn\3\2\2\2no\3\2\2\2op\7\f\2\2p\"\3\2\2\2\16\2\63\67:@DGLR`"+
		"hm\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}