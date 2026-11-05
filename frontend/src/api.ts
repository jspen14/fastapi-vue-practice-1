export interface RootResponse {
  message: string
}

export async function fetchRoot(): Promise<RootResponse> {
  const response = await fetch('/api')
  if (!response.ok) {
    throw new Error(`Request failed (${response.status})`)
  }
  return (await response.json()) as RootResponse
}
