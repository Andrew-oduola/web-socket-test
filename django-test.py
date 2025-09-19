import asyncio, websockets, json

JWT_TOKEN = """eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU4NjM1MTM5LCJpYXQiOjE3NTgyNzUxMzksImp0aSI6IjU5NzVjYjRhNzIzMjQxNmQ5YjYxZjc0MWIwMGU5OTc3IiwidXNlcl9pZCI6IjhhODM3YWQ0LTA1OWEtNGE4ZC1hZGEwLWQ4ZjhjNTM3OTMxNiIsImVtYWlsIjoiYXlvYmFtaW9kdW9sYTE3QGdtYWlsLmNvbSIsImlzX2VtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc19jb21wbGV0ZV9wcm9maWxlIjpmYWxzZSwiaXNfa3ljX3ZlcmlmaWVkIjpmYWxzZSwiaXNfcGhvbmVfdmVyaWZpZWQiOmZhbHNlLCJpc19hZGRyZXNzX3ZlcmlmaWVkIjpmYWxzZSwiZmlyc3RfbmFtZSI6bnVsbCwibGFzdF9uYW1lIjpudWxsLCJ1c2VybmFtZSI6bnVsbH0.Kxv9drMyohCRhx-eIfJoiHOzRdP1LY0pm4Xoa0W04SA"""
CONVERSATION_ID = "cf0b4b79-092d-44cc-99d5-51f092c6b495"

async def test_ws():
    uri = f"ws://127.0.0.1:8000/ws/chat/{CONVERSATION_ID}/?token={JWT_TOKEN}"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"message": "Hello with JWT"}))
        print(await websocket.recv())

asyncio.run(test_ws())
