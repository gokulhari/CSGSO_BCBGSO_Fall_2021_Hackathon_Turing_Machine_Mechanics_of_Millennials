// Generated from eqSolver.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link eqSolverParser}.
 */
public interface eqSolverListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link eqSolverParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(eqSolverParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link eqSolverParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(eqSolverParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link eqSolverParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(eqSolverParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link eqSolverParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(eqSolverParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code building_exp}
	 * labeled alternative in {@link eqSolverParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBuilding_exp(eqSolverParser.Building_expContext ctx);
	/**
	 * Exit a parse tree produced by the {@code building_exp}
	 * labeled alternative in {@link eqSolverParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBuilding_exp(eqSolverParser.Building_expContext ctx);
	/**
	 * Enter a parse tree produced by the {@code num_exp}
	 * labeled alternative in {@link eqSolverParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNum_exp(eqSolverParser.Num_expContext ctx);
	/**
	 * Exit a parse tree produced by the {@code num_exp}
	 * labeled alternative in {@link eqSolverParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNum_exp(eqSolverParser.Num_expContext ctx);
	/**
	 * Enter a parse tree produced by the {@code paran_exp}
	 * labeled alternative in {@link eqSolverParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParan_exp(eqSolverParser.Paran_expContext ctx);
	/**
	 * Exit a parse tree produced by the {@code paran_exp}
	 * labeled alternative in {@link eqSolverParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParan_exp(eqSolverParser.Paran_expContext ctx);
	/**
	 * Enter a parse tree produced by the {@code iden_exp}
	 * labeled alternative in {@link eqSolverParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIden_exp(eqSolverParser.Iden_expContext ctx);
	/**
	 * Exit a parse tree produced by the {@code iden_exp}
	 * labeled alternative in {@link eqSolverParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIden_exp(eqSolverParser.Iden_expContext ctx);
}