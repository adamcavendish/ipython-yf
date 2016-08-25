import ast
import asyncio

yield_from_fname = "ipython_extension_yf_yield_from"

class RewriteYieldFrom(ast.NodeTransformer):
    def visit_YieldFrom(self, node):
        ret = ast.Call(ast.Name(yield_from_fname, ast.Load()), [node.value], [])
        ret.lineno = node.lineno
        ret.col_offset = node.col_offset
        ast.fix_missing_locations(ret)
        return ret

    def visit_FunctionDef(self, node):
        return node

def yield_from(coro):
    if not hasattr(yield_from, 'original_loop'):
        yield_from.original_loop = asyncio.get_event_loop()
        loop = asyncio.SelectorEventLoop()
        asyncio.set_event_loop(loop)
        ret = yield_from(coro)
        asyncio.set_event_loop(yield_from.original_loop)
        del yield_from.original_loop
        return ret
    loop = asyncio.get_event_loop()
    try:
        ret = loop.run_until_complete(coro)
    finally:
        pass
    return ret

def load_ipython_extension(ip):
    ip.ast_transformers.append(RewriteYieldFrom())
    ip.user_global_ns[yield_from_fname] = yield_from

