from aiohttp import web

async def hello(request):
    
    return web.json_response({
        "message" : "Hello"
    })

if __name__ == "__main__":

    app = web.Application()
    app.router.add_get("/", hello)
    web.run_app(app)
