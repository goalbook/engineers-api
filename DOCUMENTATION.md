# Engineers API

The engineers API is an API that provides info about Goalbook engineers.

## API Reference

### Get Engineer By ID

```HTTP
GET /engineer/:id
```

**Response**

```ts
{
  _id: string
  // The first name of the engineer
  first_name: string
  // The last name of the engineer
  last_name: string
  // the location the engineer is based out of
  location: string
}
```