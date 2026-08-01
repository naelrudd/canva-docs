Source: https://www.canva.dev/docs/apps/creating-audio-tracks/

> ## Documentation Index
> Fetch the complete documentation index at: https://www.canva.dev/docs/apps/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating audio tracks

How to add audio tracks to a user's design.

Apps can add audio tracks to a user's design. These audio tracks play while the user is presenting their design and when the design is [exported](https://www.canva.dev/docs/apps/exporting-designs/) as a video.

<Note>
  To embed audio from third-party sources, such as Spotify, see [Embedding rich media](https://www.canva.dev/docs/apps/embedding-rich-media/).
</Note>

## The user experience

When an app creates an audio track, the audio file is uploaded to the user's media library.

The user's media library has a storage quota. If the user has a [Canva Pro](https://www.canva.com/pro/) account, their storage quota is 1TB. Otherwise, their storage quota is 5GB. If the user exceeds the storage quota, they'll see an error.

The audio track itself appears in the design's timeline.

## Supported audio formats

Apps can add the following types of audio to a user's design:

| Name      | MIME type   | Common file extensions        |
| --------- | ----------- | ----------------------------- |
| MPEG      | audio/mpeg  | .mpg, .mpeg, .mp1, .mp2, .mp3 |
| MP4 Audio | audio/mp4   | .mp4, .m4a                    |
| M4A       | audio/x-m4a | .m4a                          |
| MP3       | audio/mp3   | .mp3                          |
| OGG       | audio/ogg   | .ogg, .oga                    |
| WAV       | audio/wav   | .wav                          |
| X-WAV     | audio/x-wav | .wav                          |
| WEBM      | audio/webm  | .webm                         |

The maximum size of an audio file is 250MB.

## Feature support considerations

Apps can only add audio tracks to fixed [design types](https://www.canva.dev/docs/apps/designs/#design-types), such as Presentations. To learn more, see [Feature support](https://www.canva.dev/docs/apps/feature-support/).

## How to create audio tracks

### Step 1: Enable the required scopes

In the Developer Portal, enable the following scopes:

* `canva:design:content:write`
* `canva:asset:private:write`

In the future, the Apps SDK will throw an error if the required scopes aren't enabled.

To learn more, see [Configuring scopes](https://www.canva.dev/docs/apps/configuring-scopes/).

### Step 2: Upload an audio file

Import the `upload` method from the `@canva/asset` package:

```ts
import { upload } from "@canva/asset";
```

Call the method, passing in the options shown here:

```ts
const result = await upload({
  type: "audio",
  title: "Example audio",
  url: "https://www.canva.dev/example-assets/audio-import/audio.mp3",
  mimeType: "audio/mp3",
  durationMs: 86047,
  aiDisclosure: "none"
});
```

When uploading audio, the URLs must be exposed via the internet and available to Canva's backend, as Canva needs access to the URLs to download them. This means you can't use `localhost` URLs.

The `upload` method returns an object that contains a `ref` property:

```ts
console.log(result.ref);
```

This property contains a *reference*, which is a unique identifier that points to an audio asset in Canva's backend. An app can use this reference to interact with the file — even while it's uploading.

### Step 3: Add the audio track to the design

Import the `addAudioTrack` method from the `@canva/design` package:

```ts
import { addAudioTrack } from "@canva/design";
```

Call the method, passing in the options shown here:

```ts
await addAudioTrack({
  ref: result.ref,
});
```

The only required property is the `ref` property.

## Additional considerations

* All audio files must comply with Canva's [Acceptable Use Policy](https://www.canva.com/policies/acceptable-use-policy/).
* All audio files must comply with Canva's [Terms of Use](https://www.canva.com/policies/terms-of-use/).

## API reference

* [`addAudioTrack`](https://www.canva.dev/docs/apps/api/latest/design-add-audio-track/)
* [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/)

## Code sample

```tsx
import { Button, Rows } from "@canva/app-ui-kit";
import { useFeatureSupport } from "@canva/app-hooks";
import { upload } from "@canva/asset";
import { addAudioTrack } from "@canva/design";

export function App() {
  const isSupported = useFeatureSupport();
  async function handleClick() {
    const result = await upload({
      // Upload an audio file
      type: "audio",
      title: "Example audio",
      url: "https://www.canva.dev/example-assets/audio-import/audio.mp3",
      mimeType: "audio/mp3",
      durationMs: 86047,
      aiDisclosure: "none",
    });
    if (isSupported(addAudioTrack)) {
      await addAudioTrack({
        // Add the audio track to the design
        ref: result.ref,
      });
      return;
    }
  }

  return (
    <Rows spacing="1u">
      <Button
        variant="primary"
        onClick={handleClick}
        disabled={!isSupported(addAudioTrack)}
      >
        Add Audio Track
      </Button>
    </Rows>
  );
}
```
