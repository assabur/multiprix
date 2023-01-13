# Multiprix

The target of this project is to give insight about the different offers in France on mobile, fiber and ADSL.
We should have a snapshot, and some evolutions.

To do that, data are scrapped from internet sites of operators, data are stored quite in clickhouse, cleaned, merged, and displayed on http://multiprix.datax.iliad.fr


See the project issues.


# Guidance

- Clean code
- KISS over DRY
- When there is a choice to make (ex: add or create a library, split code, refactorize function ), make explicit tradeoffs and document it in the issue in gitlab. It should not be discovered later when reviewd
- When in Rome, do as the Romans do. ex:
    - use list/dict comprehension in python
    - in typescript, create type or so
    - use pandas rich api
- Attention to details :
    -   edge cases
    -   variable naming ex : "u" for very local variable like in map or liust comprehension, user for function variable, 
- Functional over OPP:
    - code should be primary factorized in pure function
- Test, but test behavior, not implementation, and do mostly integration
