# mongoDB

## Structure

The sor is always included as type.
[type]

### config collection

GuildId is always included in config as guildId.
[guildId]

#### prefix

[prefix]

#### JoinRoles

[roleId]

#### manageCommands

[command, roles]

#### selfCommandRoles

[role, commandRolesObject]

#### betterVc

[categoryId]

#### deletePinned

[]

#### deletingChannel

[channelId]

### league

#### player

[discordId, mmr]

#### matches

[[[discordId...],[discordId...]],winningTeam]

### stats

GuildId is always included in config as guildId.
[guildId]

All the same with different actions
